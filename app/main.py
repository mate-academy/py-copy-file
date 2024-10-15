def copy_file(command: str) -> None:
    command = command.split()
    if command[0] != "cp":
        raise ValueError("You line should start with cp")
    if len(command) != 3:
        raise ValueError("Message should be: cp <source_file> <destination_file>")
    if command[1] == command[2]:
        raise ValueError("There should be two different names of files")
    elif ".txt" in (command[1] and command[2]):
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            file_out.write(file_in.read())
