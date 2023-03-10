def copy_file(command: str) -> None:
    file_names = command.split()
    if file_names[1] != file_names[2]:
        with (open(file_names[1], "r") as file1,
              open(file_names[2], "w") as file2):
            file2.write(str(file1))
