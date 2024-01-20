def copy_vile(command: str) -> None:
    if len(command.split()) != 3:
        return

    operation, source_name, new_file_name = command.split()
    if operation == "cp" and source_name != new_file_name:
        with (
            open(source_name, "r") as source,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(source.read())
