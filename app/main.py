def copy_file(command: str) -> None:
    cp, file, file_copy = command.split(" ")

    if file == file_copy or cp != "cp":
        return

    with open(file, "r") as file_in, open(file, "w") as file_out:
        file_out.write(file_in.read())
