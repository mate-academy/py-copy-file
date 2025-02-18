def copy_file(command: str):
    split = command.split(" ")
    existing_file_name = split[1]
    new_file_name = split[2]
    if existing_file_name != new_file_name and split[0] == "cp":
        with open(existing_file_name, "r") as ex_file,\
                open(new_file_name, "w") as new_f:
            new_f.write(ex_file.read())
