def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_name, target_name = parts[1], parts[2]

    if source_name == target_name:
        return

    try:
        with (open(source_name, "r") as file_in,
              open(target_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
