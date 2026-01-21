def copy_file(command: str):

    command_list = command.split()
    cp = command_list[0]
    first_file = command_list[1]
    second_file = command_list[2]

    if cp != "cp" or first_file == second_file:
        return None

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())
