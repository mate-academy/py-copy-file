def copy_file(command: str) -> None:
    try:
        command, current_file, copy_of_file = command.split()
    except ValueError:
        return

    if command == "cp" and current_file != copy_of_file:
        with open(current_file, "r") as file_in, open(
            copy_of_file, "w"
        ) as file_out:
            file_out.write(file_in.read())
