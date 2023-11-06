def copy_file(command: str) -> None:
    files_names = command.split()
    if files_names[1] == files_names[2]:
        return

    with (open(files_names[1], "r") as main_file,
          open(files_names[2], "w") as copied_file):
        for line in main_file:
            copied_file.write(line)
