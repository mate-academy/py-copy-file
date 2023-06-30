def copy_file(command: str) -> None:
    command_info, file_current, file_copy = command.split()

    if file_current != file_copy and command_info == "cp":
        with (
             open(file_current, "r") as file_in,
             open(file_copy, "w") as file_out
             ):
            file_out.write(file_in.read())
