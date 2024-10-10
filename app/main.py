def copy_file(command: str) -> None:
    command = command.split(" ")
    cp = command[0]
    file_from = command[1]
    file_to = command[2]
    if cp == "cp" and file_from != file_to:
        with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
            file_to.write(file_from.read())
