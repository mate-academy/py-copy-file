def copy_file(str_of_files: str):
    files = str_of_files.split()
    if files[0] == files[1]:
        return
    else:
        with open(files[0], "r") as file_in, open(files[1], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
