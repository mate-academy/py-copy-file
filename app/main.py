def copy_file(command: str) -> str:
    split_command = command.split()
    if len(split_command) != 3 or split_command[1] == split_command[2] or split_command[0] != "cp":
        return "Error, information entered incorrectly"
    try:
        with open(split_command[1], "r") as f1, open(split_command[2], "w") as f2:
            info_to_copy = f1.read()
            f2.write(info_to_copy)
    except FileNotFoundError:
        print(f"File {split_command[1]} not found.")
