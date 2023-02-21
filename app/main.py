def copy_file(string: str) -> None:
    command, file_name, new_file_name = string.split()
    if command == "cp" and file_name != new_file_name:
        with (open(f"{file_name}", "r") as file,
             open(f"{new_file_name}", "w") as new_file):
            new_file.write(file.read())
