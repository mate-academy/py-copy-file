def copy_file(command: str):
    sep_command = command.split()
    file = sep_command[1]
    new_file = sep_command[2]

    if file != new_file:
        with open(file, "r") as f:
            with open(new_file, "w") as f2:
                f2.write(str(f.read()))


if __name__ == '__main__':
    copy_file("cp file.txt file1.txt")
