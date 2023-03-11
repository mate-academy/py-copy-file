def copy_file(command: str) -> None:
    string_list = command.split(" ")
    if len(string_list) == 3 and string_list[0] == "cp":
        if string_list[1] != string_list[2]:
            with open(string_list[1], "r") as file_in, \
                    open(string_list[2], "w") as file_out:
                file_in = file_in.read()
                file_out.write(file_in)
