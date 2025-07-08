def copy_file(command: str) -> None:
    try:
        command, original_filename, copy_filename = command.split(" ")
    except ValueError:
        return

    if command != "cp" or original_filename == copy_filename:
        return

    try:
        with (open(original_filename, "r") as original_file,
              open(copy_filename, "w") as copy_file):
            copy_file.write(original_file.read())
    except FileNotFoundError:
        return
