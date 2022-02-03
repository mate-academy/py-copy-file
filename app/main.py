def copy_file(command: str):
    command_list = command.split(" ")
    if command_list[0] != "cp":
        print("Enter correct command (cp)")
    elif command_list[1] != command_list[2]:
        with open(command_list[1], "r") as first_file:
            file_content = first_file.read()
            with open(command_list[2], "w") as second_file:
                second_file.write(file_content)


if __name__ == '__main__':
    copy_file("cp file.txt file1.txt")
