def copy_file(command_string: str) -> str:
    command, original_file, copy_file = command_string.split()
    if command == "cp" and original_file != copy_file:
        with (
            open(original_file, "r") as copy_from,
            open(copy_file, "w") as copy_to
        ):
            copy_to.write(copy_from.read())
