import shutil


def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "cp":
        _, src_file, dest_file = command_parts
        if src_file == dest_file:
            return

        with open(src_file, "r") as src, open(dest_file, "w") as dest:
            shutil.copyfileobj(src, dest)


copy_file("cp file.txt new_file.txt")
