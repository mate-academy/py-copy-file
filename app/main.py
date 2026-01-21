def copy_file(command: str) -> None:
    command, copied, file_to_copy = command.split()
    if copied != file_to_copy or command == "cp":
        with open(copied, "r") as file_in, open(file_to_copy, "w") as file_out:
            file_out.write(file_in.read())
