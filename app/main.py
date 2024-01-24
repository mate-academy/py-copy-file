def copy_file(command: str):
    action, file_name, new_file_name = command.split(" ")

    if file_name == new_file_name and action != "cd":
        return None

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_content = file_in.readlines()
        for line in file_content:
            file_out.write(line)
