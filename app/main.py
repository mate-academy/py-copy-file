def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) != 3 or split_command[0] != "cp":
        print("Invalid command")
        return

    file_to_copy = split_command[1]
    copied_file = split_command[2]

    if file_to_copy == copied_file:
        return

    with open(file_to_copy, "r") as file, open(copied_file, "w") as copy:
        copy.write(file.read())
