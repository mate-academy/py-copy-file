def copy_file(command: str):
    file_names = command.split()

    if file_names[1] != file_names[2]:
        with open(file_names[1], "r") as f_in, \
                open(file_names[2], "w") as f_out:
            f_out.write(f_in.read())
