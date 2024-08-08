def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        print(f"Expected 3 arguments, got {len(command_parts)}")
        return

    command, old_file, new_file = command_parts

    if command != "cp":
        print(f"Expected 'cp' command, got {command}")
        return

    if old_file == new_file:
        print(f"File {new_file} already exists")
        return

    try:
        with open(old_file, "r") as file_in:
            with open(new_file, "w") as file_out:
                file_out.write(file_in.read())
    except OSError:
        raise OSError(f"File {old_file} does not exist")
