def copy_file(str_of_files: str):
    files = str_of_files.split()
    if files[1] == files[2]:
        return
    else:
        with open(files[1], "r") as file_in, open(files[2], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
