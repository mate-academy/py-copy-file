def copy_file(command: str) -> None:
    split_command = command.split()

    if split_command[1] == split_command[2]:
        pass
    else:
        with open(
                f"{split_command[1]}", "r"
        ) as initial_file, \
                open(
                    f"{split_command[2]}", "w"
        ) as copied_file:
            copied_file.write(initial_file.read() + "\n")
