def copy_file(command_str: str) -> None:
    command, input_file_name, output_file_name = command_str.split()
    if len(command_str.split()) != 3 or command != "cp":
        return
    if input_file_name == output_file_name:
        return
    with open(input_file_name, "r") as file_in, \
            open(output_file_name, "w") as file_out:
        file_out.write(file_in.read())
