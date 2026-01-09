def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_file, target_file = parts

    if source_file == target_file:
        return

    try:
        with (open(source_file, "r") as
              file_in, open(target_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
