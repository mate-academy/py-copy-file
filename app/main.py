def copy_file(command: str):

    cmd_list = command.split()
    cp = cmd_list[0]
    first_file = cmd_list[1]
    second_file = cmd_list[2]

    if cp != "cp" or first_file == second_file:
        return None

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())
