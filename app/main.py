def copy_file(command):
    prefix = command.split(" ")[0]
    old_file = command.split(" ")[1]
    new_file = command.split(" ")[2]

    if old_file == new_file or not prefix == "cp":
        return
    try:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
    except FileNotFoundError:
        print("Mentioned file does not exist")
