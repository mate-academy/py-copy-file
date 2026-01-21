def copy_files(file_names: str) -> None:
    if len(file_names.split()) == 3:
        command, file, new_file = file_names.split()
        if command == "cp" and file != new_file:
            with open(file, "r") as origin, open(new_file, "w") as copy:
                copy.write(origin.read())
