def copy_file(command: str) -> None:
    if command[0:2] != "cp" or command.count(" ") != 2:
        return
    _, file_name, copy_file = command.split(" ")
    if file_name == copy_file:
        return
    with open(file_name, "r") as file_in, open(copy_file, "w") as file_out:
        for line in file_in:
            file_out.write(f"{line}")
