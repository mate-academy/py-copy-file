def copy_file(command: str):
    listed = command.split()
    if listed[1] == listed[2]:
        return

    with open(listed[1], "r") as file_in, open(listed[2], "w") as file_out:
        file_out.write(file_in.read())
