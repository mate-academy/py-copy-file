def copy_file(command: str) -> None:
    if len(command.split(" ")) != 3:
        return
    command, source_path, destination_path = command.split(" ")
    if command == "cp" and source_path != destination_path:
        with (open(source_path, "r") as old_file,
              open(destination_path, "w") as new_file):
            new_file.write(old_file.read())
