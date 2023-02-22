def copy_file(command) -> None:
    command = command.split()
    if command[1] == command[2]:
        return
    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file1 = file_in.read()
        file_out.write(file1)
