def copy_file(command: str):
    file_data_list = command.split(" ")
    old_file = file_data_list[1]
    new_file = file_data_list[2]
    if old_file != new_file:
        with open(old_file, "r") as file_out, open(new_file, "w") as file_in:
            for line in file_out:
                file_in.write(line)
