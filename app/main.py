def copy_file(command):
    operator, file, new_file = command.split()
    if operator != "cp" or file == new_file:
        return

    with open(file, 'r') as file_to_copy:
        with open(new_file, 'w') as file_copy:
            for line in file_to_copy:
                file_copy.write(line)


def main():
    copy_file("cp test1.txt test2.txt")


if __name__ == "__main__":
    main()
