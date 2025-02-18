def copy_file(command):
    file = command.split(" ")

    command = file[0]
    old_file = file[1]
    new_file = file[2]

    if old_file != new_file and command == "ср":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
