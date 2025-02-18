def copy_file(command: str) -> None:
    cp_command, file, file_copy = command.split()
    if file != file_copy and cp_command == "cp":
        with open(file, "r") as file_in, open(file_copy, "w") as file_out:
            file_out.write(file_in.read())
