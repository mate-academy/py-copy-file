def copy_file(command: str) -> None:
    file_names = command.split()

    if file_names[1] != file_names[2]:
        with (open(file_names[1], "r") as input_file,
              open(file_names[2], "a") as output_file):
            output_file.write(input_file.read())
