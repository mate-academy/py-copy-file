import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    # Перевіряємо, що команда має правильний формат: "cp source target"
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    source_file, target_file = command_parts[1], command_parts[2]

    # Якщо джерело і цільове ім'я однакові, нічого не робимо
    if source_file == target_file:
        return

    # Перевіряємо, чи існує вихідний файл
    if not os.path.exists(source_file):
        return

    # Копіюємо файл
    with open(source_file, "r") as source, open(target_file, "w") as target:
        target.write(source.read())
