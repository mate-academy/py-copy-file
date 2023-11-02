def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    command_name, main_file, for_copy_file = parts

    if main_file == for_copy_file or command_name != "cp":
        return

    with open(main_file, "r") as source, open(for_copy_file, "w") as copy:
        copy.write(source.read())
