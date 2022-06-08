def copy_file(command):
    with open(command[3:12], 'r') as old, open(command[12:], 'a') as new:
        if old != new:
            for line in old:
                new.write(line)
