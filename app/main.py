def copy_file(command: str) -> None:
    parts_of_command = command.split()
    file_source = parts_of_command[1]
    file_new = parts_of_command[2]
    condition = [
        command[:2] == "cp",
        file_source != file_new,
        len(parts_of_command) == 3,
        ".txt" in file_source,
        ".txt" in file_new,
    ]
    if all(condition):
        with open(file_source, "r") as source, open(file_new, "w") as copied:
            for line in source.readlines():
                copied.write(line)
