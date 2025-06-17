(
  to_entries
  | map({
      key,
      value: (
        .value
        | to_entries
        | map(select(
            (.value | type == "array") and (.value[0] != 0)
          ))
        | from_entries
      )
    })
  | map(select(.value != {}))
  | from_entries
)
