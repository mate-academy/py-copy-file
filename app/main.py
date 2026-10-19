import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        action, source, destination = parts

        if action != "cp" or not os.path.exists(source):
            return

        if source == destination:
            return

        with open(source, "r", encoding="utf-8") as file_in, open(
                destination, "w", encoding="utf-8"
        ) as file_out:
            file_out.write(file_in.read())
