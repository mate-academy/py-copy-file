def copy_file(command: str) -> None:
    command_cp, file1, file2 = command.split(" ")
    if not command_cp == "cp":
        return None
    elif file1 == file2:
        return None
    else:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
