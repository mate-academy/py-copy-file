def copy_file(command: str) -> None:
    """Копіює файл згідно з командою у форматі 'cp source.txt target.txt'.

    Args:
        command: Рядок команди у форматі 'cp source.txt target.txt'.
    """
    parts: list[str] = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file: str = parts[1]
    target_file: str = parts[2]

    if source_file == target_file:
        return

    try:
        with open(source_file, mode="rb") as file_in, open(
            target_file, mode="wb"
        ) as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
