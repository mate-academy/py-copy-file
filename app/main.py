
def copy_file(command: str) -> None:
    command_parsed = command.split(" ")
    file_in_name = command_parsed[1]
    file_out_name = command_parsed[2]

    if command_parsed[0] == "cp":
        if file_in_name == file_out_name:
            return None
        else:
            with open(file_in_name, "r") as file_in, \
                 open(file_out_name, "w") as file_out:

                file_in_data = file_in.read()
                file_out.write(file_in_data)
