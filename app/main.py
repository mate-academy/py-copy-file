def copy_file(command: str):
    command = command.split(' ')
    if command[1] != command[2]:
        with open(command[1], 'r') as file:
            with open(command[2], 'w') as file_copy:
                file_copy.write(file.read())
