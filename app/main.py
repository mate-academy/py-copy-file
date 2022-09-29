def copy_file(command):
    a = command.split(" ")
    if a[1] != a[2]:
        with open(f"{a[1]}", "r") as file, open(f"{a[2]}", "w") as file_copy:
            content = file.read()
            file_copy.write(content)
