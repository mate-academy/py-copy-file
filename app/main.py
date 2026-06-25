def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source, copy = parts[1], parts[2]

    if source == copy:
        return

    try:
        with open(source, "r") as f, open(copy, "w") as g:
            g.write(f.read())
    except FileNotFoundError:
        print(f"Помилка: Файл {source} не знайдено.")
