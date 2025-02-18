def copy_file(command: str) -> None:
    # Розбиваємо команду на частини:
    # перевіряємо, чи є три елементи,
    # і чи починається з "cp"
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        # Якщо команда має неправильний формат,
        # можемо додати логування або обробку помилки
        return

    source_file = parts[1]
    destination_file = parts[2]

    # Перевіряємо, чи не однакові джерело та призначення
    if source_file == destination_file:
        # Додаємо коментар, щоб пояснити, чому ця перевірка необхідна
        return

    # Відкриваємо файли через контекстні менеджери і копіюємо вміст
    with (open(
            source_file, "r"
    ) as file_in, open(
        destination_file, "w"
    ) as file_out):
        file_out.write(file_in.read())
