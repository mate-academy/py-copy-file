def copy_file(command: str) -> None:
    cmd, file, new_file = command.split()

    if cmd == "cp" and file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
