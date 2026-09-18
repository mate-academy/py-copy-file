def copy_file(command: str) -> None:
    if len(command) != 0:
        line = command.split(" ")
    else:
        return None

    if len(line) == 3 and line[0] == "cp" and line[1] != line[2]:
        try:
            with (open(line[1], "r") as source_file,
                  open(line[2], "w") as destination_file):
                file_in = source_file.read()
                destination_file.write(file_in)
        except FileNotFoundError:
            return None
