def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "cp":
        source_file_name = command_parts[1]
        destination_file_name = command_parts[2]
        if source_file_name == destination_file_name:
            return
        try:
            with (open(source_file_name, "r") as file_in,
                  open(destination_file_name, "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            pass
