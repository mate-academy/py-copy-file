def copy_file(command):
    file_names = command.split()

    first_file, second_file = file_names[1], file_names[2]

    if first_file == second_file:
        with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
            file_out.write(file_in.read())