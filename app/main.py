def copy_file(command: str):
    command_list = command.split(" ")
    if command_list[0] != "cp":
        print("Enter correct command (cp)")
    elif command_list[1] != command_list[2]:
        with open(command_list[1], "r") as file:
            file_lines = file.readlines()
            with open(command_list[2], "w") as file2:
                file2.write("".join(file_lines))


if __name__ == '__main__':
    copy_file("cp file.txt file1.txt")
