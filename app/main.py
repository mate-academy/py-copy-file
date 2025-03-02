def copy_file(command: str) -> None:
    split_command = command.split()

    try:
        if split_command[0] != "cp" or split_command[1] == split_command[2]:
            return None

        with (open(split_command[1], "r") as current_file,
              open(split_command[2], "w") as new_file):
            current_file_content = current_file.read()

            new_file.write(current_file_content)
    except (FileNotFoundError, IndexError):
        return
