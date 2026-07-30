def copy_file(command: str) -> None:
    command_data = command.split()

    if len(command_data) < 3:
        return

    cp, current_file, new_file = command_data

    if cp != "cp":
        return

    if current_file == new_file:
        return

    try:
        with (
            open(current_file, "r") as file_in,
            open(new_file, "w") as file_out,
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not found.")
