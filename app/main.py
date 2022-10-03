def copy_file(command):
    files = command.split(" ")[1::]
    old_file = files[0]
    new_file = files[1]
    if old_file != new_file and command == f"cp {old_file} {new_file}":
        with open(old_file, "r") as old_file:
            with open(new_file, "w") as new_file:
                new_file.write(old_file.read())
