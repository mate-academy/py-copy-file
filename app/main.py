def copy_file(command: str) -> None:
    parts = command.split()
    source_file, target_file = parts[1], parts[2]
    if source_file == target_file:
        return
    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
