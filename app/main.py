def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Invalid command format. Use 'cp source_file target_file'"
        )

    source_file, target_file = parts[1:]

    if source_file == target_file:
        return

    with (open(source_file, "r", encoding="utf-8") as file_in,
          open(target_file, "w", encoding="utf-8") as file_out):
        file_out.write(file_in.read())
