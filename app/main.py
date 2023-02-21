def copy_file(command: str) -> None:
    if len(command) != 3:
        raise ValueError("Invalid command value")
    interim, command_file, copied_file = command
    file_to_copy = interim[2]
    if command_file == "cp" and copied_file != file_to_copy:
        with (
            open(copied_file, "r") as file_r,
                open(file_to_copy, "w") as file_w
        ):
            file_w.write(file_r.read())
