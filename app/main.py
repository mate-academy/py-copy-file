def copy_file(files):
    files_name = files.split(" ")
    if files_name[0] == "cp" and files_name[1] != files_name[2]:
        with open(files_name[1], "r") as file_in, \
                open(files_name[2], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
