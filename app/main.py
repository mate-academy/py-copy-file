def copy_file(command: str) -> None:
    command, file, copied_file = command.split("")
    if command not in "cp":
        raise ValueError(f"Not correct command: {command}")
    if file != copied_file:
        with (open(file, "r") as reading_file,
              open(copied_file, "w") as writing_file):
            writing_file.write(reading_file.read())
