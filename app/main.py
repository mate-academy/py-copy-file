def copy_file(command: str):
    file_names = command.split(" ")

    if file_names[1] != file_names[2]:
        with open(file_names[1], "r") as f:
            with open(file_names[2], "w") as f2:
                f2.write(f.read())


copy_file("cp test.txt test-copy.txt")
