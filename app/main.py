def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        command_name = command[0]
        file_copy = command[1]
        file_new = command[2]

        if command_name == "cp" and file_new != file_copy:

            with (
                open(file_copy, "r") as file_in,
                open(file_new, "w") as file_out
            ):
                data = file_in.read()
                file_out.write(data)
