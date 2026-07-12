import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        source_file_name = parts[1]
        destination_file_name = parts[2]
        if os.path.exists(source_file_name):
            if source_file_name != destination_file_name:
                with (open(source_file_name, "r") as file_in,
                      open(destination_file_name, "w") as file_out):
                    file_out.write(file_in.read())
