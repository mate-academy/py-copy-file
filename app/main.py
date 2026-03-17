def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_filename = parts[1]
    target_filename = parts[2]
    try:
        if source_filename != target_filename:
            with (open(source_filename, "r") as file_in,
                  open(target_filename, "w") as file_out):
                file_out.write(file_in.read())
    except FileNotFoundError:
        return
