def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        raise ValueError(f"Expected 3 arguments, got {len(command_parts)}")

    command, old_file, new_file = command_parts
    if old_file == new_file:
        raise ValueError(f"File {new_file} already exists")

    try:
        with open(old_file, "r") as file_in:
            with open(new_file, "w") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"File {old_file} does not exist")