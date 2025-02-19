import os


def copy_file(command: str) -> None:
    # Разбиваем строку команды
    parts = command.split()

    # Проверяем, что команда имеет правильный формат
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, target_file = parts[1], parts[2]

    # Если пытаемся скопировать файл сам в себя — ничего не делаем
    if source_file == target_file:
        return

    # Проверяем, существует ли исходный файл
    if not os.path.exists(source_file):
        return

    # Копируем содержимое файла
    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
