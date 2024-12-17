def copy_name(command: str) -> None:
    parts = command.split(" ")

    source_file, new_file = parts[1], parts[2]

    if source_file == new_file:
        return

    with open(source_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
