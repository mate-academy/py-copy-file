def copy_file(command: str) -> None:
    command = command.split()
    if command[0] != "cp" or len(command) != 3:
        raise ValueError("Invalid input")
    file_from = command[1]
    file_to = command[2]
    if file_from == file_to:
        print("Does Nothing")
    with (
        open(f"{file_from}", "r") as file_from,
        open(f"{file_to}", "w") as file_to
    ):
        file_to.write(file_from.read())
