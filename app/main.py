from shutil import copy


def copy_file(command: str) -> str:
    split_command = command.split()

    if len(split_command) != 3:
        return "Invalid command"

    source_file, destination_file = split_command[1:]

    if source_file == destination_file:
        return "Source and destination files are the same."

    try:
        copy(source_file, destination_file)
        return f"File copied successfully"
    except FileNotFoundError:
        return f"The source file: {source_file} does not exist"
    except PermissionError:
        return f"Permission denied for {destination_file}"
