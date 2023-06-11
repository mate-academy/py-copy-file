def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise ValueError("Command shold have three arguments")
    if command[0] != "cp":
        raise ValueError("It is not cp command")
    if command[1] != command[2]:
        with (open(command[1], "r") as source,
              open(command[2], "w") as copy):
            copy.write(source.read())
