def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3:
        parameter, old_file, new_file = split_command

        if parameter != "cp":
            raise ValueError("Parameter must be 'cp'")

        if old_file == new_file:
            raise ValueError("old_file and new_file must have different names")

        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
