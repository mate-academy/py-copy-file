def copy_file(command: str) -> None:
    command, copied_file, file_to_copy = command.split()
    if command == "cp" and copied_file != file_to_copy:
        with (open(copied_file, "r") as file_r,
                open(file_to_copy, "w") as file_w):
            file_w.write(file_r.read())
