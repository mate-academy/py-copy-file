import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, destination_file_name = parts[1], parts[2]
    if (source_file_name == destination_file_name
            or not os.path.exists(source_file_name)):
        return

    with (open(source_file_name, "r") as file_in,
          open(destination_file_name, "w") as file_out):
        for line in file_in:
            file_out.write(line)
