def copy_file(command: str):
    parse_list_parameters = command.split(" ")
    if len(parse_list_parameters) != 3:
        raise Exception("Invalid command string. "
                        "Expected cp file_name_from file_name_to")
    if parse_list_parameters[1] == parse_list_parameters[2]:
        raise Exception("Invalid command string. "
                        "file_name_from and file_name_to have same names")
    with open(parse_list_parameters[1], "r") as file_in, \
            open(parse_list_parameters[2], "w") as file_out:
        file_out.write(file_in.read())
