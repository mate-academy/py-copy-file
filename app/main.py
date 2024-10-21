def copy_file(command: str) -> None:
    name_f = command.split()[1]
    new_f = command.split()[2]
    if new_f == name_f:
        return
    with open(name_f, "r") as file_in, open(new_f, "w") as file_out:
        file_out.write(file_in.read())
