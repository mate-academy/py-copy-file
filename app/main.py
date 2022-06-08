def copy_file(command):
    with open(command[3:12], 'r') as first, open(command[12:], 'a') as second:
        if first != second:
            for line in first:
                second.write(line)
