def copy_file(command: str) -> None:
    file_name = command.split()[1]
    new_file = command.split()[2]
    if new_file == file_name:
        return
    if command.split()[0] == "cp":
        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    else:
        return
