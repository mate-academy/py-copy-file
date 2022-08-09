def copy_file(command: str):
    file_name_in, file_name_out = command.split()[1:]

    if file_name_in and file_name_out and file_name_in != file_name_out:
        with open(file_name_in, "r") as file_in,\
                open(file_name_out, "w") as file_out:
            file_out.write(file_in.read())
