def copy_file(command: str) -> None:
    file_name = command.split()[1]
    file_copy_name = command.split()[2]

    if file_name == file_copy_name:
        return

    with open(file_copy_name, "r") as file_in, \
            open(file_name, "w") as file_out:
        file_in.write(file_out.read())
