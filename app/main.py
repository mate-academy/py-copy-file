def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    action, origin_file, new_file = parts
    if origin_file != new_file:
        try:
            with open(origin_file, "r") as orig, open(new_file, "w") as cop:
                content = orig.read()
                cop.write(content)
        except FileNotFoundError as err:
            print(err)
