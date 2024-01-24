def copy_file(command: str) -> None:
    try:
        cp, main_file, for_copy_file = command.split()
    except ValueError:
        return

    if main_file == for_copy_file:
        return

    with open(main_file, "r") as source, open(for_copy_file, "w") as copy:
        copy.write(source.read())
