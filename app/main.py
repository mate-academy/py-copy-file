def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return  # Неверная команда — ничего не делаем

    src, dst = parts[1], parts[2]

    if src == dst:
        return  # Копировать в тот же файл не нужно

    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"File not found: {src}")
