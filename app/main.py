
def copy_file(command: str):
    file = command.split()[1]
    new_file = command.split()[2]
    if file != new_file and command.split()[0] == "cp":
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            # shutil.copyfile()
            file_out.write(file_in.read())
