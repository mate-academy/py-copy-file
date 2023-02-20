def copy_file(command: str) -> None:
    cmd, old_file, new_file = command.split(" ")
    if cmd == "cp" and old_file != new_file:
        with open(old_file, "r") as file_out, open(new_file, "w") as file_in:
            file_in.write(file_out.read())
