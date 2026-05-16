from __future__ import annotations


def copy_file(command: str) -> None:
    command_parts = command.split()

    # Перевіряємо, чи команда має рівно 3 частини і чи починається вона з 'cp'
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    source_file = command_parts[1]
    destination_file = command_parts[2]

    if source_file == destination_file:
        return

    # Відловлюємо відсутність файлу, а контекстний менеджер розбиваємо дужками,
    # щоб довжина рядка не перевищувала 79 символів (вимога Flake8)
    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out,
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
