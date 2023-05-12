def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "cp":
        return
    print(split_command)  # перевірка на наявність 3 аргументів в split_command
    original_file = split_command[1]
    new_file = split_command[2]
    if original_file == new_file:
        return
    with open(original_file, "r") as file_in, open(new_file, "w") as file_out:
        file_in.write(file_out.read())
