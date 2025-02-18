def copy_file(command: str) -> None:
    command_parts = command.split()
    command, old_file, new_file = command_parts
    if len(command_parts) == 3 and command == "cp" and old_file != new_file:
        try:
            with open(old_file, "r") as file_in:
                with open(new_file, "w") as file_out:
                    file_out.write(file_in.read())
        except OSError:
            raise OSError(f"File {old_file} does not exist")
