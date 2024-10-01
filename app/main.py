def copy_file(files_names: str) -> None:
    command, file, new_file = files_names.split()
    if command == "cp" and file != new_file:
        with (open(file, "r") as original,
              open(new_file, "w") as copy):
            copy.write(original.read())
