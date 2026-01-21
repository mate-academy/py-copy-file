def copy_file(command: str) -> None:
    parts: list[str] = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file: str = parts[1]
    target_file: str = parts[2]

    if source_file == target_file:
        return

    try:
        with open(source_file, "r", encoding="utf-8") as file_in, \
                open(target_file, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("Source file not found.")
