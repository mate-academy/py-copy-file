def copy_file(command: str) -> None:

    if len(command.split()) == 3:
        command_name, file_copy, file_new = command.split()

        if command_name == "cp" and file_new != file_copy:

            with (
                open(file_copy, "r") as file_in,
                open(file_new, "w") as file_out
            ):
                file_out.write(file_in.read())
