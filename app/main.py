def copy_file(copy_files: str):
    cp_file = copy_files.split(" ")
    if cp_file[1] != cp_file[2]:
        with open(cp_file[1], "r") as file_in,\
                open(cp_file[2], "w") as file_out:
            file_out.write(file_in.read())
