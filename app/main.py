def copy_file(command: str):
    file_names = command.split()

    if file_names[1] != file_names[2]:
        with open(file_names[1], "r") as file_in:
            with open(file_names[2], "w") as file_out:
                data = file_in.read()
                file_out.write(data)
