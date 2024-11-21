def copy_file(command: str):
    check_list = command.split()
    if check_list[1] != check_list[2]:
        with open(check_list[1], "r") as file_in:
            lines = file_in.readlines()

        with open(check_list[2], "w") as file_out:
            for line in lines:
                file_out.write(line)
