def copy_file(command: str):
    lst_separated = command.split(" ")
    if lst_separated[1] != lst_separated[2]:
        with open(lst_separated[1], "r") as first_file, \
                open(lst_separated[2], "a") as second_file:
            for line in first_file:
                second_file.write(line)
