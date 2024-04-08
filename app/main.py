def copy_file(command: str) -> None:
    file_in, file_out = command.split()[1], command.split()[2]
    with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
        file_out.write(file_in.read())