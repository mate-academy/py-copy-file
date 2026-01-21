import os


def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        cmd, source_file_name, destination_file_name = parts
        if source_file_name == destination_file_name:
            return
        if os.path.exists(source_file_name):
            with (open(source_file_name, "r") as input_file,
                  open(destination_file_name, "w") as output_file):
                for line in input_file:
                    output_file.write(line)
