def copy_file(command):
    operator, file, new_file = command.split()
    if operator != "cp" or file == new_file:
        return

    with open(file, 'r') as f:
        with open(new_file, 'w') as f2:
            for line in f:
                f2.write(line)


def main():
    copy_file("cp test1.txt test1.txt")


if __name__ == "__main__":
    main()
