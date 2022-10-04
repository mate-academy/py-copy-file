def copy_file(command: str):
    names = command.split()
    file = names[1]
    file_copy = names[2]
    with open(file, "r") as file_in, open(file_copy, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
