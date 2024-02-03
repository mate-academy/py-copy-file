def copy_file(command: str) -> None:
    command, file, copy = command.split(" ")
    if command == "cp" and file != copy:
        with open(file, "r") as f, open(copy, "w") as c:
            file_info = f.read()
            c.write(file_info)
