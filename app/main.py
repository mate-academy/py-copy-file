def copy_file(command):
    split_file = command.split(" ")
    file = split_file[1]
    new_file = split_file[2]
    if file != new_file:
        with open(file, "r") as file_out, open(new_file, "r") as file_in:
            text = file_out.read()
            file_in.write(text)
