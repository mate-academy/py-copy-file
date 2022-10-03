def copy_file(command):
    command = input()
    list = command.split()
    if list[1] != list[2]:
        with open(f"{list[1]}", "r") as file_to_copy, \
                open(f"{list[2]}", "a") as result_file:
            for line in file_to_copy:
                result_file.write(line)
