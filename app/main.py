import os


def copy_file(command: str) -> None:
    parts = command.split()

    # 1. Проверка формата команды
    if len(parts) != 3:
        return

    cmd, source_file, target_file = parts

    # 2. Проверка что это именно cp
    if cmd != "cp":
        return

    # 3. Нельзя копировать в тот же файл
    if source_file == target_file:
        return

    # 4. Проверка существования source файла
    if not os.path.exists(source_file):
        return

    # 5. Копирование
    with open(source_file, "r", encoding="utf-8") as file_in, \
         open(target_file, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
