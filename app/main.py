def copy_file(command):
    command = command[3:].split(" ")
    with open(command[0], 'r') as old, open(command[1], 'a') as new:
        if old != new:
            for line in old:
                new.write(line)
