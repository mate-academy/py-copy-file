def copy_file(command: str) -> None:
    cp, old_file, new_file = command.split()

    if cp != "cp":
        raise ValueError("The command need to start with 'cp'")

    if command.split() != 3:
        raise ValueError("Command format needs to be <cp file_1 file_2>")

    if old_file != new_file:
        with open(old_file, "r") as source_file, open(new_file, "w") as destination_file:
            destination_file.write(source_file.read())
