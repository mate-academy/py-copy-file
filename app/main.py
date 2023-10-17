def copy_file(command: str) -> None:
    command, filename, new_filename = command.split()
    if command == "cp" and filename != new_filename:
        with (open(filename, "rb") as source,
              open(new_filename, "wb") as destination):
            destination.write(source.read())
