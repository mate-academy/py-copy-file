def copy_file(command: str) -> None:
    file_name = command.split()
    if len(file_name) == 3:
        if file_name[0] == "cp" and file_name[1] != file_name[2]:
            with (
                open(file_name, "r") as file_in,
                open(file_name, "w") as file_out
            ):
                file_to_read = file_in.read()
                file_out.write(file_to_read)
