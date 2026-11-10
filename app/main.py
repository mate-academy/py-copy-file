def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    name_one = parts[1]
    name_two = parts[2]
    if parts[0] == "cp":
        if name_one == name_two:
            return

        try:
            with (open(name_one, "r") as file_in,
                  open(name_two, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
        except FileNotFoundError:
            return
