def copy_file(command: str) -> None:
    action, source_file, destination_file = command.split()
    if action == "cp" and source_file != destination_file:
        with open(source_file, "rb") as src_file, (
                open(destination_file, "wb")
        ) as dest_file:
            while True:
                data = src_file.read()
                if not data:
                    break
                dest_file.write(data)
