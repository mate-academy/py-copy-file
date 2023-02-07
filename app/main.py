def copy_file(command: str) -> None:
    """Copies the contents of one file to another"""

    # checking for correct command structure
    if command.count(" ") > 2 or command.count(" ") < 2:
        return "wrong command"

    # separate the command and file names
    command, old_file, new_file = command.split(" ")

    # check that the file names do not match
    if old_file == new_file:
        return

    # check whether the file names and commands are specified correctly
    if old_file.endswith(".txt") \
            and new_file.endswith(".txt") \
            and command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    else:
        return "wrong command"
