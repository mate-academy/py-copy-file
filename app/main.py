def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        original = command.split()[1]
        copy = command.split()[2]
        if original != copy:
            with open(original, "r") as file_in, open(copy, "w") as file_out:
                file_out.write(file_in.read())
