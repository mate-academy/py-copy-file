def copy_file(command: str) -> None:
    name_in, name_out = command.split()[1:]
    if name_in == name_out:
        return
    with open(name_in, "r") as file_in, open(name_out, "w") as file_out:
        file_out.write(file_in.read())
