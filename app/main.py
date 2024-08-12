def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3:
        command, source_file, destination = parts

    if len(parts) != 3 or command != "cp":
        print("Invalid command!")
        return

    if source_file == destination:
        return

    with open(source_file, "r") as f, open(destination, "w") as f_copy:
        f_copy.write(f.read())
