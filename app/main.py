def copy_file(command: str) -> None:
    line_to_copy = command.split(" ")
    if line_to_copy[0] != "cp" or line_to_copy == "" or len(line_to_copy) != 3:
        return
    else:
        new_file_name = line_to_copy[-1]
        copied_file_name = line_to_copy[1]
        if new_file_name == copied_file_name:
            return
        try:
            with (open(copied_file_name, "r") as file,
                  open(new_file_name, "w") as new_file):
                new_file.write(file.read())
        except FileNotFoundError:
            return
