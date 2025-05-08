import json
import redfish
from logging import getLogger

log = getLogger(__name__)

def is_hex(param):
    import string
    return all(c in string.hexdigits for c in param)

def trim_supermicro_key(key):
    return key[:-5] if (key[-5] == "_" and is_hex(key[-4])) else key

def trim_supermicro_dict(settings_dict):
    return {trim_supermicro_key(k): v for k, v in settings_dict.items()}

class RedFishBMC(object):
    def __init__(self, hostname, username=None, password=None, arch_override=None):
        self.name = hostname
        self.username = username
        self.password = password
        self.redfish = redfish.redfish_client(
            base_url="https://" + hostname,
            username=username,
            password=password,
            default_prefix='/redfish/v1')
        try:
            self.redfish.login(auth="session")
        except redfish.rest.v1.InvalidCredentialsError:
            log.error(f"Error logging into {hostname} - invalid credentials")
            raise
        except Exception as exc:
            log.error(f"Error logging into {hostname}: {exc}")
            raise

        self.vendor = next(iter(self.redfish.root.get("Oem", {}).keys()), None) or self.redfish.root.get("Vendor", None)

        self.systems_uri = self.redfish.root['Systems']['@odata.id']
        self.systems_response = self.redfish.get(self.systems_uri)
        self.systems_members_uri = next(iter(self.systems_response.dict['Members']))['@odata.id']
        self.systems_members_response = self.redfish.get(self.systems_members_uri)
        self.bios_version = self.systems_members_response.dict.get('BiosVersion', None)

        self.systems_members_response_actions = self.systems_members_response.dict['Actions']
        try:
            self.system_reset_types = self.systems_members_response_actions['#ComputerSystem.Reset']['ResetType@Redfish.AllowableValues']
        except KeyError:
            self.system_reset_action_info = self.redfish.get(self.systems_members_response_actions['#ComputerSystem.Reset']['@Redfish.ActionInfo'])
            self.system_reset_types = self.system_reset_action_info.dict['Parameters'][0]['AllowableValues']

        self.proc_uri = self.systems_members_response.dict['Processors']['@odata.id']
        self.proc_data = self.redfish.get(self.proc_uri)
        self.proc_members_uri = next(iter(self.proc_data.dict['Members']))['@odata.id']
        self.proc_members_response = self.redfish.get(self.proc_members_uri)

        if arch_override:
            self.arch = arch_override
        else:
            model = self.proc_members_response.dict.get("Model")
            if model and isinstance(model, str):
                self.arch = "AMD" if model.startswith("A") else "Intel"
            else:
                log.warning(f"[{self.name}] Unable to determine CPU architecture, defaulting to AMD")
                self.arch = "AMD"

        self.bios_uri = self.systems_members_response.dict['Bios']['@odata.id']
        self.bios_data = self.redfish.get(self.bios_uri)

        if 'error' in self.bios_data.dict:
            raise Exception(f"Error fetching BIOS settings for {self.name}: {self.bios_data.dict['error']['@Message.ExtendedInfo']}")

        self.bios_settings_uri = self.bios_data.dict.get('@Redfish.Settings', {}).get('SettingsObject', {}).get('@odata.id', None)
        self.supported_apply_times = self.bios_data.dict.get('@Redfish.Settings', {}).get('SupportedApplyTimes', None)

        self.managers_uri = self.redfish.root['Managers']['@odata.id']
        self.managers_data = self.redfish.get(self.managers_uri)
        self.managers_members_uri = next(iter(self.managers_data.dict['Members']))['@odata.id']
        self.managers_members_response = self.redfish.get(self.managers_members_uri)
        self.managers_members_actions = self.managers_members_response.dict['Actions']

    def print_settings(self):
        print(f"{self.name} Current BIOS settings:")
        print(json.dumps(self.bios_data.obj.Attributes, indent=4, sort_keys=True))

    def check_settings(self, settings):
        log.info(f"Checking BIOS settings on {self.name}")
        if settings is None:
            log.info(f"{self.name}: No settings provided for this platform")
            return 0
        count = 0
        if self.vendor == "Supermicro":
            settings = self.adjust_supermicro_settings(settings)
            if settings is None:
                return 0
        for key, value in settings.items():
            if key not in self.bios_data.obj.Attributes:
                log.error(f"{self.name}: Desired key ({key}) is not part of BIOS settings")
            elif self.bios_data.obj.Attributes[key] != value:
                log.info(f"{self.name}: BIOS setting {key} is {self.bios_data.obj.Attributes[key]}, should be {value}")
                count += 1
        return count

    def change_settings(self, settings_dict):
        if self.vendor == "Supermicro":
            settings_dict = self.adjust_supermicro_settings(settings_dict)
            if settings_dict is None:
                return False
        body = {'Attributes': settings_dict}
        if self.supported_apply_times and "OnReset" in self.supported_apply_times:
            body["@Redfish.SettingsApplyTime"] = {"ApplyTime": "OnReset"}
        resp = self.redfish.patch(self.bios_settings_uri, body=body)
        if resp.status == 400:
            try:
                print(json.dumps(resp.dict['error']['@Message.ExtendedInfo'], indent=4, sort_keys=True))
            except Exception as exc:
                log.error(f"Extended error info not available: {exc}")
        elif resp.status in [200, 201, 202]:
            log.info(f"Settings updated on {self.name}; reboot required")
            return True
        else:
            log.error(f"Unexpected response {resp.status}")
        return False

    def reset_settings_to_default(self):
        resp = self.redfish.post(self.bios_actions_dict['#Bios.ResetBios']['target'], body=None)
        return resp.status in [200, 201, 202, 204]

    def reboot(self):
        action = self.systems_members_response.obj.Actions['#ComputerSystem.Reset']['target']
        body = {'ResetType': 'GracefulRestart' if 'GracefulRestart' in self.system_reset_types else 'ForceRestart'}
        resp = self.redfish.post(action, body=body)
        return resp.status in [200, 201, 202, 204]

    def adjust_supermicro_settings(self, settings_dict):
        adjusted = {}
        for key, val in settings_dict.items():
            mapped = self.supermicro_find_key(trim_supermicro_key(key))
            if mapped:
                adjusted[mapped] = val
            else:
                log.error(f"{self.name}: Unable to map Supermicro key {key}")
        return adjusted if adjusted else None

    def supermicro_find_key(self, key):
        for k in self.bios_data.obj.Attributes.keys():
            if "_" in k and k.startswith(key + "_") and is_hex(k[-4:]):
                return k
            if k == key:
                return k
        return None