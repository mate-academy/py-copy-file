def copy_file(command: str):
    command_line = command.split()
    command = command_line[0]
    first_filename = command_line[1]
    second_filename = command_line[2]
    if command == "cp" and first_filename != second_filename:
        with open(first_filename, "r") as file_in, \
             open(second_filename, "w") as file_out:
            file_out.write(file_in.read())
