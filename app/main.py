def copy_file(full_command: str) -> None:
    command, source_name, new_file = full_command.split(" ")
    if source_name == new_file:
        return
    source = open(source_name, "r")
    with source as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
