def copy_file(command):
    s_list = command.split(" ")
    file_in = s_list[1]
    file_out = s_list[2]
    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        cont = f_in.read()
        f_out.write(cont)
