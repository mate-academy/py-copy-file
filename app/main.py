def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "cp":
        return print("Wrong command!")
    if split_command[1] == split_command[2]:
        return
    with open(f"{split_command[1]}", "r") as file_in:
        content = file_in.read()
    with open(f"{split_command[2]}", "w") as file_out:
        file_out.write(str(content))
