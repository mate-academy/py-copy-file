def copy_file(command: str):
    file_1 = command.split()[1]
    file_2 = command.split()[2]

    if not file_1 == file_2:
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
