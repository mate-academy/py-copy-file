def copy_file(command: str) -> None | str:
    short_command, name_f_in, name_f_out = command.split()
    if short_command != "cp":
        return "Write correct command"
    if name_f_in == name_f_out:
        return "the name of the second file must not be the same as the first"
    with open(name_f_in, "r") as file_in, open(name_f_out, "w") as file_out:
        file_out.write(file_in.read())
