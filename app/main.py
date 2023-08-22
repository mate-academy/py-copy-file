def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, name_to_copy, new_file_name = command.split()
        if command_name == "cp" and name_to_copy != new_file_name:
            with (
                open(name_to_copy, "r") as file_in,
                open(new_file_name, "w") as file_out
            ):
                file_out.write(file_in.read())
