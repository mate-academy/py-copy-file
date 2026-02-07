def copy_file(command: str) -> None:
    temp = command.split()

    if len(temp) != 3:
        return

    copy, source_file, target_file = temp

    if copy != "cp" or source_file == target_file:
        return

    try:
        with (open(source_file, "r", encoding="utf-8") as file,
              open(target_file, "w", encoding="utf-8") as out):
            out.write(file.read())
    except FileNotFoundError:
        return
