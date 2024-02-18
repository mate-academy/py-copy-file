def copy_file(files_name: str) -> None:
    files_name = files_name.split(" ")
    if len(files_name) == 3 \
            and files_name[1] != files_name[2] \
            and files_name[0] == "cp":
        with open(str(files_name[1]), "r") as file_read, \
                open(str(files_name[2]), "w") as file_write:
            file_write.write(file_read.read())
