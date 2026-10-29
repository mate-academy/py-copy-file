
def copy_file(command: str) -> None:
    split_command: list[str] = command.split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    source_file_name = split_command[1]
    destination_file_name = split_command[2]

    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as file_in,
              open(destination_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
