def copy_file(command: str):
    origin_file = command.split()[1]
    file_copy = command.split()[2]

    if origin_file != file_copy:
        with open(origin_file, "r") as f:
            with open(file_copy, "w") as c:
                c.write(f.read())
