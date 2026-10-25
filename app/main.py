def copy_file(command: str) -> None:
    split_command = command.split()
    if (len(split_command) == 3
        and split_command[0] == "cp"
            and split_command[1] != split_command[2]):

        try:
            with (open(split_command[1], "r") as file_for_copy,
                  open(split_command[2], "w") as file_copy):
                file_copy.write(file_for_copy.read())
        except FileNotFoundError:
            pass
