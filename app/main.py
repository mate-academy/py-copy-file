def copy_file(command: str) -> bool:
    parts = command.split()
    if parts[0] == "cp":
        old_file, new_file = parts[1], parts[2]

        if old_file != new_file:
            with open(old_file, "r") as file_old, open(new_file, "w") as file_new:
                file_new.write(file_old.read())
