def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    cp, file_name1, file_name2 = parts
    if file_name1 == file_name2 or cp != "cp":
        return
    try:
        with (open(file_name1, "r") as source_file,
              open(file_name2, "w") as dest_file):
            for line in source_file:
                dest_file.write(line)
    except FileNotFoundError:
        return
