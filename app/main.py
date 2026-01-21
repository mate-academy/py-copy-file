def copy_file(command: str) -> None:
    file_names = command.strip().split()

    if len(file_names) != 3 or file_names[0] != "cp":
        return

    if file_names[1] == file_names[2]:
        return

    try:
        with (open(file_names[1], "r") as input_file,
              open(file_names[2], "a") as output_file):
            output_file.write(input_file.read())
    except FileNotFoundError:
        return
