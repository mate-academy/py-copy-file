def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, destination_file_name = parts[1], parts[2]
    if source_file_name == destination_file_name:
        return

    with open(source_file_name, "r", encoding="utf-8") as file_in, open(destination_file_name, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
