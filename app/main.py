def copy_file(command: str) -> None:
    interim = command.split()
    command_file = interim[0]
    copied_file = interim[1]
    file_to_copy = interim[2]
    if command_file == "cp" and copied_file != file_to_copy:
        with (
            open(copied_file, "r") as file_r,
                open(file_to_copy, "w") as file_w
        ):
            file_w.write(file_r.read())
