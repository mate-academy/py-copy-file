def copy_file(command: str) -> None:
    command_cp, file_old, file_new = command.split()
    if file_old != file_new and command_cp == "cp":
        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            file_out.write(file_in.read())
