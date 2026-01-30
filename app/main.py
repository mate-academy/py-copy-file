def copy_file(command: str) -> None:
    filenames = command.split(" ")
    if len(filenames) != 3 or filenames[0] != "cp":
        return
    original_filename = filenames[1]
    new_filename = filenames[2]
    if original_filename == new_filename:
        return
    try:
        with (open(original_filename, "r") as file_in,
              open(new_filename, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
