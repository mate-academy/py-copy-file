def copy_file(command: str) -> None:
    split_command = command.split()
    if (len(split_command) == 3
            and split_command[0] == "cp"
            and split_command[1] != split_command[2]):
        with (
            open(f"{split_command[1]}", "r") as initial_file,
            open(f"{split_command[2]}", "w") as copied_file
        ):
            copied_file.write(initial_file.read())
