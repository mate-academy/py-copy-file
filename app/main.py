def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) == 3:
        command, source_file, destination_file = command_list

        if source_file != destination_file and command == "cp":
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                file_out.write(file_in.read())
