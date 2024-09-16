def copy_file(command):
    file = command.split(" ")[1]
    file_copy = command.split(" ")[2]
    if file != file_copy:
        with open(file, "r") as origin:
            text = origin.read()
            with open(file_copy, "w") as copy:
                copy.write(text)


copy_file("cp file.txt file-copy.txt")
