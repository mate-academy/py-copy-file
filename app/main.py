def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise ValueError("Command should have three arguments")
    cp, file_from, file_in = command
    if cp != "cp":
        raise ValueError("It is not cp command")
    if file_from != file_in:
        with (open(file_from, "r") as source,
              open(file_in, "w") as copy):
            copy.write(source.read())
