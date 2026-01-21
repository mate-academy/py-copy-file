def copy_file(command: str) -> None:
    line = command.split()
    if not line or line[0] != "cp" or len(line) != 3:
        return
    source_file, target_file = line[1], line[2]
    if source_file == target_file:
        return
    try:
        with open(source_file, "r") as file_in, \
                open(target_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
