def copy_file(command: str) -> None:
    files_names = command.split()
    if (len(files_names) == 3 and files_names[0] == "cp"
            and files_names[1] != files_names[2]):
        first_file, second_file = files_names[1], files_names[2]
        with (open(first_file, "r") as original,
              open(second_file, "w") as copied):
            copied.write(original.read())
