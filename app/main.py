def copy_file(command: str) -> None:
    prefix = command.split()[0]
    file_name = command.split()[1]
    copy_file_name = command.split()[2]
    if file_name != copy_file_name and prefix == "cp":
        with (
            open(file_name, "r") as file_in,
            open(copy_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())
