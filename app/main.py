def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    command_name, first_file, second_file = command.split()
    if first_file == second_file or command_name != "cp":
        return
    try:
        with (
            open(first_file, "r") as file_in,
            open(second_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except (FileExistsError, FileNotFoundError):
        return
