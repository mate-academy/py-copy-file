def copy_file(command: str) -> None:
    _, file, copy = command.split(" ")
    if file != copy:
        with open(file, "r") as file_in, open(copy, "w") as file_out:
            file_out.write(file_in.read())
