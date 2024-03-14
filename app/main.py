def copy_file(command: str):
    files = command.split()
    command = files[0]
    first_file = files[1]
    new_file = files[2]

    if first_file == new_file or command != "cp":
        return None

    with open(first_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
    return "Complete!"
