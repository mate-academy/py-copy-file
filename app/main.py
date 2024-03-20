def copy_file(command: str) -> None:
    file_names = command.split()
    if file_names[1] != file_names[2] and file_names[0] == "cp":
        with (open(file_names[1], "r") as file,
              open(file_names[2], "w") as new_file):
            new_file.write(file.read())
