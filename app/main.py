def copy_file(command: str) -> None:
    action, source_file, destination_file = command.split()
    if action == "cp" and source_file != destination_file:
        with open(source_file, "rb") as src_file, (
                open(destination_file, "wb")
        ) as dest_file:
            dest_file.write(src_file.read())
