def copy_file(command: str) -> None:
    list_files = command.split()
    if list_files[1] != list_files[2]:
        with open(list_files[1], "r") as f1, open(list_files[2], "w") as f2:
            f2.write(f1.read())
