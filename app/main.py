import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " cp <source_file> <destination_file>")

    _, source_file, test_file = parts

    if source_file == test_file:
        raise ValueError("Source and destination files have the same name. "
                         "No action taken.")

    try:
        shutil.copyfile(source_file, test_file)
        print(f"File '{source_file}' copied to '{test_file}' successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: One or both of the files"
                                f" '{source_file}' and '{test_file}' "
                                f"not found.")
