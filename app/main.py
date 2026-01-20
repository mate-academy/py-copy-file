def copy_file(command: str) -> None:
    parts = command.split(" ")

    command, source_file, new_file = parts[0], parts[1], parts[2]

    if command != "cp" and len(parts) != 3:
        return

    if source_file == new_file:
        return

    with open(source_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
