def copy_file(command: str) -> None:
    command_parts = command.split()
    _, source_file, destination_file = command_parts

    if source_file == destination_file:
        return
    with open(
            source_file,
            "r"
    ) as file_in, open(
        destination_file,
        "w"
    ) as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt file1.txt")
