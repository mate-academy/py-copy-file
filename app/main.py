def copy_file(command: str) -> bool:
    parts = command.split()
    if parts[0] == "cp":
        old_file, new_file = parts[1], parts[2]

        if old_file != new_file:
            with open(old_file, "r") as file_in, open(new_file, "w") as file:
                file.write(file_in.read())
            return open(old_file).read() == open(new_file).read()
