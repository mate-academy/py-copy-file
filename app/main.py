def copy_file(command):
    old_file_name = command.split()[1]
    new_file_name = command.split()[2]

    if old_file_name == new_file_name:
        return

    with open(old_file_name, "r") as f:
        with open(new_file_name, "w") as f2:
            f2.write(f.read())
