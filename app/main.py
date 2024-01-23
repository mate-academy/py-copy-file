def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    main_file = parts[1]
    for_copy_file = parts[2]

    if main_file == for_copy_file:
        return

    with open(main_file, "r") as source, open(for_copy_file, "w") as copy:
        copy.write(source.read())
