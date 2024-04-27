def copy_file(command: str) -> None:
    files = command.split()
    if len(files) != 3:
        raise Exception("The command line must have 3 parameters")
    input_command, old_file, new_file = files

    if old_file != new_file and input_command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            new_file = file_out.write(file_in.read())
