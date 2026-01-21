def copy_file(command: str):
    file = command.split(" ")
    command, old_file, new_file = file[0], file[1], file[2]

    if old_file != new_file and command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
