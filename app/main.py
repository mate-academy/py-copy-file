import os


def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        source_file_name = command_parts[1]
        destination_file_name = command_parts[2]
        if command_parts[0] == "cp":
            if source_file_name == destination_file_name:
                return None
            else:
                if os.path.exists(source_file_name):
                    with (open(source_file_name, "r") as file_in,
                         open(destination_file_name, "w") as file_out):
                        text_read = file_in.read()
                        file_out.write(text_read)
                else:
                    return None
        else:
            return None
    else:
        return None
