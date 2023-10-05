def copy_file(filename: str) -> None:
    files = filename.split(" ")[1:]
    if files[1] != files[2]:
        with open(files[1], "r") as file_in, \
             open(files[2], "w") as file_out:
            file_out.write(file_in.read())
