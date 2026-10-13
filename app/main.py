def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3:
        return

    origin_archive = parts[1]
    destine_archive = parts[2]

    if origin_archive == destine_archive:
        return

    try:
        with open(origin_archive, "r", encoding="utf-8") as entry, \
                open(destine_archive, "w", encoding="utf-8") as out:

            final_archive = entry.read()
            out.write(final_archive)

    except FileNotFoundError:
        return
