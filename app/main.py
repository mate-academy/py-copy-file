def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    if parts[1] == parts[2]:
        return

    source_file_name = parts[1]
    target_file_name = parts[2]

    try:
        with (open(source_file_name, "r") as input_file,
              open(target_file_name, "w") as output_file):
            content = input_file.read()
            output_file.write(content)
    except FileNotFoundError:
        return
