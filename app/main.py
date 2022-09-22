def copy_file(command):
    name_in, name_out = command.split()[1:]

    if name_in == name_out:
        return

    with open(name_in, "r") as file_in, open(name_out, "w") as file_out:
        for line in file_in:
            file_out.write(line)
