def copy_file(command: str) -> None | ValueError:
    if command.split()[0] != "cp" or len(command.split()) != 3:
        raise ValueError("Invalid command format")

    original, copy = command.split()[1], command.split()[2]
    if original == copy:
        return

    with open(original, "r") as file_in, open(copy, "w") as file_out:
        file_out.write(file_in.read())
