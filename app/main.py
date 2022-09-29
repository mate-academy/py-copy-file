def copy_file(command):
    string = command.strip().split(" ")
    file1 = string[1]
    file2 = string[2]
    if string[0] == "cp":
        if file1 != file2:
            with open(f"{file1}", "r") as file, open(f"{file2}", "w") as file_copy:
                content = file.read()
                file_copy.write(content)
