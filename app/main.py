import os


def copy_file(command: str) -> None:
    parts = command.split()

    # Ожидаемо формат: cp source destination
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    # Якщо назви однакові — ничого не робимо
    if source == destination:
        return

    # Якщо вхідного файла немає — ничего не робимо
    if not os.path.exists(source):
        return

    # Копируемо контент
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
