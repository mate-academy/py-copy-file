def copy_file(command: str) -> None:
    try:
        command, source_file_name, destination_file_name = command.split()
    except ValueError:
        print("Wrong command format")
    else:
        if command == "cp" and source_file_name != destination_file_name:
            with (
                open(source_file_name) as source_file,
                open(destination_file_name, "w") as destination_file
            ):
                destination_file.write(source_file.read())
