def copy_file(command: str) -> None:
    # Розділити команду на окремі частини
    tokens = command.split()

    # Перевірка коректності формату команди
    if len(tokens) != 3 or tokens[0] != "cp":
        return

    # Вилучити імена файлів
    source = tokens[1]
    dest = tokens[2]

    # Якщо файли однакові - нічого не робити
    if source == dest:
        return

    try:
        # Відкрити вихідний файл для читання
        with open(source, "rb") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        # Якщо файл не знайдено - просто вийти без дій
        return

    # Записати зчитаний вміст у новий файл
    with open(dest, "wb") as file_out:
        file_out.write(content)
