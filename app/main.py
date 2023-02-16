def copy_file(command: str) -> None:

    # Split command line into three parts
    cmd, file_name, copy_file_name = command.split()

    # Do nothing when user is trying to copy file to file with the same name
    if file_name == copy_file_name:
        return

    # Raise exception for invalid command
    if cmd != "cp":
        raise ValueError(f"Wrong command, {cmd} != 'cp'")

    # Make copy file
    with open(file_name) as file, open(copy_file_name, "w") as new_file:
        new_file.write(file.read())
