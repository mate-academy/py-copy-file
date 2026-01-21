def copy_file(command: str):
    props = command.split()
    file_name = props[1]
    new_file_name = props[2]

    if file_name != new_file_name:
        with open(file_name, "r") as origin_file:
            with open(new_file_name, "w") as file_copy:
                text = origin_file.read()
                file_copy.write(text)
