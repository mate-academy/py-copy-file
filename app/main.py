def copy_file(command: str) -> None:
    """Copies the contents of one file to another"""

    # we check the command structure
    if len(command.split()) != 3:
        return "wrong command"

    # separate the command and file names
    command, old_file, new_file = command.split(" ")

    # check that the file names do not match
    if old_file == new_file:
        return "the file names do match"

    # checking if the command name is correct
    if command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    else:
        return f"unknown command '{command}'"
