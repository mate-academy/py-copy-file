def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return  # Невірна команда — нічого не робимо

    source_filename, destination_filename = parts[1], parts[2]

    if source_filename == destination_filename:
        return  # Не копіюємо файл у самого себе

    try:
        with (open(source_filename, "r", encoding="utf-8")
              as file_in, open(
            destination_filename,
            "w", encoding="utf-8"
        ) as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
