def copy(command: str) -> None:
    cmd, file, new_file = command.split()
    if file != new_file or cmd == "cp":
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
