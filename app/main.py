def copy_file(command: str):
    temp = command.split()
    if temp[-1] == temp[-2]:
        pass
    else:
        with open(f"{temp[-2]}", 'r') as file_in, \
                open(f"{temp[-1]}", 'w') as file_out:
            file_out.write(f"{file_in.read()}")
