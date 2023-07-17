def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "cp":
        original, copy = command.split()[1], command.split()[2]
        if original != copy:
            with open(original, "r") as file_in, open(copy, "w") as file_out:
                file_out.write(file_in.read())
