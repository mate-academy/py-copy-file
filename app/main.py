def copy_file(command: str) -> None:
    try:
        command, main_file, for_copy_file = command.split()
    except ValueError:
        return
    if command != "cp" or main_file == for_copy_file:
        return

    with open(main_file, "r") as source, open(for_copy_file, "w") as copy:
        copy.write(source.read())
