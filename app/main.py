def copy_file(command: str) -> None:

    command_name, file1, file2 = command.split(" ")

    if command_name != "cp" or file1 == file2:
        return None

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
