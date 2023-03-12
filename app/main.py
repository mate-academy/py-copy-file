def copy_file(command: str) -> None:
    string_list = command.split(" ")
    instruct = string_list[0]
    file_in_name = string_list[1]
    file_out_name = string_list[2]
    if len(string_list) == 3 and instruct == "cp":
        if file_in_name != file_out_name:
            with open(file_in_name, "r") as file_in, \
                    open(file_out_name, "w") as file_out:
                file_in = file_in.read()
                file_out.write(file_in)
