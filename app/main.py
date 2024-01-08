def copy_file(command: str) -> None:
    split_command = command.split()
    if split_command[0] == "cp":
        if split_command[1] != split_command[2]:
            with (open(split_command[1], "r") as file1,
                  open(split_command[2], "w") as file2):
                file2.write(file1.read())
