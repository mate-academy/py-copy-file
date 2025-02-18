import shutil


def copy_file(command: str):
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format. Use: 'cp source_file destination_file'")

    source, destination = parts[1], parts[2]

    if source == destination:
        return  # Do nothing if source and destination are the same

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
