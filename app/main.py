def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, target_file_name = parts[1], parts[2]

    if source_file_name == target_file_name:
        return

    try:
        with (open(source_file_name, "r") as source_file,
              open(target_file_name, "w") as target_file):
            for line in source_file:
                target_file.write(line)
    except FileNotFoundError:
        return
