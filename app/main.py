def copy_file(command: str):
    command_list = command.split(" ")
    if command_list[0] != "cp":
        print("Enter correct command (cp)")
    elif command_list[1] != command_list[2]:
        with open(command_list[1], "r") as source:
            file_content = source.read()
            with open(command_list[2], "w") as destination:
                destination.write(file_content)


if __name__ == '__main__':
    copy_file("cp file.txt file1.txt")
