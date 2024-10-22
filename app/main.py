def copy_file(command: str) -> None:
    cmd, copy_from, copy_to = command.split()
    if cmd == "cp" and copy_from != copy_to:
        with open(copy_from, "r") as file_from, open(copy_to, "w") as file_to:
            content = file_from.read()
            file_to.write(content)
