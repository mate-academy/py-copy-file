def copy_file(command: str):
    sep_command = command.split()
    file = sep_command[1]
    new_file = sep_command[2]

    if file != new_file:
        with open(file, "r") as source:
            with open(new_file, "w") as copy:
                copy.write(str(source.read()))


if __name__ == '__main__':
    copy_file("cp file.txt file1.txt")
