from os import path


def copy_file(command: str) -> None:
    if len(command) == 0:
        return

    command_parts = command.split(" ")
    if (command_parts[0] != "cp"
            or len(command_parts) != 3
            or command_parts[1] == command_parts[2]
            or not path.exists(command_parts[1])):
        return

    source_file_name = command_parts[1]
    destination_file_name = command_parts[2]

    with (open(source_file_name, "r") as file_in,
          open(destination_file_name, "w") as file_out):
        file_out.write(file_in.read())
