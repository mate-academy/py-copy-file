def copy_file(command: str) -> None:
    try:
        command, original_file, copy_file = command.split()
    except ValueError:
        return

    if command == "cp" and original_file != copy_file:
        with open(original_file, "r") as file_in, open(
            copy_file, "w"
        ) as file_out:
            file_out.write(file_in.read())
