def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Неправильний формат команди. "
              "Очікується: cp <ім'я_файлу> <нове_ім'я_файлу>")
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"Помилка: Файл {source_file} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при копіюванні: {e}")
