def copy_file(command: str) -> bool:
    c_args = command.split()
    if command == "" or c_args[0] != "cp" or c_args[1] == c_args[2]:
        return False
    file1, file2 = c_args[1], c_args[2]
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())


# if copy_file("cp requirements.txt test1.txt"):
#    print("file copied!")
