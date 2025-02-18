def copy_file(command: str) -> None:
    command, file_in, file_out = command.split()
    if file_in != file_out and command == "cp":
        with open(file_in, "r") as file_in, open(file_out, "a") as file_out:
            file_out.write(file_in.read())
