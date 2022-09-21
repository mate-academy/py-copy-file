def copy_file(command):
    file_to_copy = command.split()[1]
    new_file = command.split()[2]
    if file_to_copy == new_file:
        return
    with open(file_to_copy, "r") as file_one, open(new_file, "a") as file_two:
        for line in file_one:
            file_two.write(line)
