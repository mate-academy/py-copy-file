def copy_file(command: str) -> None:
    parts = command.split()

    # Перевірка 1: Чи команда починається з "cp" та чи має рівно 3 частини
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    destination_file = parts[2]

    # Перевірка 2: Якщо імена файлів однакові — нічого не робимо
    if source_file == destination_file:
        return

    try:
        # Відкриваємо файли лише після того, як всі перевірки пройдено
        with open(source_file, "r", encoding="utf-8") as file_in, \
             open(destination_file, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
