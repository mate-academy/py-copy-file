def copy_file(command: str) -> None:
    command = command.split(" ")
    name_from = command[1]
    name_to = command[2]
    if command[1] == command[2]:
        pass
    with open(name_from, "r") as file_in, open(name_to, "w") as file_out:
        file_out.write(file_in.read())
