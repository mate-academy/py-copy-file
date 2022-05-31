def copy_file(command):
    src = command.split()[1]
    dst = command.split()[2]
    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())
