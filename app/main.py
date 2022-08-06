def copy_file(command):
    result = command.split(" ")
    old_file = result[1]
    new_file = result[2]
    if old_file != new_file:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            text = old.read()
            new.write(text)
