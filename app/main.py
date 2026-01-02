def copy_file(files: str):
    files = files.split()
    if files[1] == files[0]:
        return
    with open(files[0], "r") as file_in, open(files[1], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
