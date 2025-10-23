def copy_file(command: str) -> None:
    """
    Copies a file's content to another file based on a 'cp' command.

    Example: "cp source.txt destination.txt"
    Does nothing if the source and destination file names are the same.
    """
    parts = command.split()
    
    # 1. Перевіряємо, чи команда коректна (має бути 3 частини)
    if len(parts) != 3 or parts[0] != "cp":
        # Можна додати обробку помилки, але за умовою просто нічого не робимо
        return

    source_file = parts[1]
    dest_file = parts[2]

    # 2. Не робимо нічого, якщо імена файлів однакові
    if source_file == dest_file:
        return

    # 3. Копіюємо вміст
    try:
        # Використовуємо подвійний менеджер контексту, як у підказці
        with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
            
    except FileNotFoundError:
        # Обробляємо випадок, якщо вихідний файл не знайдено
        print(f"Error: File '{source_file}' not found.")
    except IOError as e:
        # Обробляємо інші помилки читання/запису
        print(f"Error copying file: {e}")
