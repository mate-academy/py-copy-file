def copy_file(command: str):
    if command:
        names = command.split(" ")
        with open(f"{names[1]}", "r") as file, \
                open(f"{names[2]}", "w") as f_copy:
            if names[1] != names[2]:
                f_copy.write(file.read())
    else:
        return "command entered incorrectly"
