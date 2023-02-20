def copy_file(command: str) -> None:
    command, old_value, new_value = command.split()
    if command == "cp" and old_value != new_value:
        with open(old_value, "r") as file_in, open(
            new_value, "w"
        ) as file_out:
            file_out.write(file_in.read())
