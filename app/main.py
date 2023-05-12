def copy_file(command: str) -> None:
    if "cp" not in command:  # перевірка на наявність команди cp в command
        return
    split_command = command.split()
    print(split_command)  # перевірка на наявність 3 аргументів в split_command
    file_1 = split_command[1]
    file_2 = split_command[2]
    if file_1 == file_2:
        return
    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        for line in file_in:
            file_out.write(line)
