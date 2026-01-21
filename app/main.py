def copy_file(command: str) -> None:
    files_names = command.split()
    if files_names[1] != files_names[2]:
        with (open(files_names[1], "r") as file_in,
             open(files_names[2], "w") as file_out):
            file1 = file_in.read()
            file_out.write(file1)
