def copy_file(command: str) -> None:
    commands = command.split()
    if not len(commands) == 3:
        raise ValueError("Three variables are required: "
                         "command, current filename, new filename.")
    else:
        cmd, name_file, new_name_file = commands
    if cmd != "cp":
        raise ValueError("Invalid command. There must be: cp.")
    elif name_file == new_name_file:
        raise ValueError("The filenames must be different.")
    else:
        with (open(name_file, "r") as file_in,
              open(new_name_file, "w") as file_out):
            file_out.write(file_in.read())
