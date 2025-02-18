def copy_file(command_str: str) -> None:
    """
    Copies content from one file to another based on the 'cp' command input.

    Args:
    - command_str (str): Command string in the
    format 'cp source_file target_file'.

    Returns:
    - None: If the command is invalid or source/target files are the same.
    """
    command_parts = command_str.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_file, target_file = command_parts

    if source_file == target_file:
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
