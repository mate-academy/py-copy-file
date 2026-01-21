def copy_file(command: str) -> None:
    split_command = command.strip().split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    source_file_name = split_command[1]
    destination_file_name = split_command[2]

    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as source_file,
              open(destination_file_name, "w") as destination_file):
            destination_file.write(source_file.read())
    except Exception:
        return
