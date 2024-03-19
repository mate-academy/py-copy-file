def copy_file(command: str) -> None:
    command, file, copied_file = command.split(" ")
    if file != copied_file:
        with (open(file, "r") as reading_file,
              open(copied_file, "w") as writing_file):
            reading_file_data = reading_file.read()
            writing_file.write(reading_file_data)
