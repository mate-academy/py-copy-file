def copy_file(command):
    data = command.split()
    if data[0] == 'cp' and data[1] != data[2]:
        with open(data[1], 'r') as source:
            with open(data[2], 'w') as result:
                result.write(str(source.read()))

if __name__ == "__main__":
    copy_file("cp file.txt file1.txt")
