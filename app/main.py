def copy_file(command: str) -> None:
    """
    Copy a file based on a command string in the format: 'cp source.txt
    destination.txt'

    Args:
        command: String containing 'cp', source file name, and destination
        file name separated by spaces
    """
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        pass
