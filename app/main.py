def copy_file(command: str) -> None:
    cmd_name, copy, paste = command.split()
    if copy != paste and cmd_name == "cp" and len(command.split()) == 3:
        with open(copy, "r") as file_in, open(paste, "w") as file_out:
            file_out.write(file_in.read())
