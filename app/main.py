def copy_file(command: str) -> None:
    file_list = command.split()
    if file_list[0] != "cp":
        print("Incorrect command")
    if file_list[1] == file_list[2]:
        pass
    with open(file_list[1], "w+") as file_in, \
         open(file_list[2], "w") as file_out:
        save_data = file_in.read()
        file_out.write(save_data)
