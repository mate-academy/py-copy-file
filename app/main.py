def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Проверка корректности команды
    if len(parts) != 3 or parts[0] != "cp":
        return

    src, dst = parts[1], parts[2]

    # Если имена совпадают — ничего не делаем
    if src == dst:
        return

        # Копирование содержимого
    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
