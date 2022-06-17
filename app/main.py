from os import remove


def copy_file(command):
    if command.split()[1] != command.split()[2]:
        old_file = open(command.split()[1], 'r')
        new_file = open(command.split()[2], "w")
        new_file.write(old_file.read())
        old_file.close()
        remove(command.split()[1])
        new_file.close()
    return "Files names is identical"
