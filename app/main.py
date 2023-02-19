def copy_file(command: str) -> None:
    try:
        cp_command, current_file, future_file = command.split()
        if current_file == future_file or cp_command != "cp":
            return
        with open(
                current_file, "r"
        ) as file, open(
            future_file, "w"
        ) as new_file:
            new_file.write(file.read())
    except AttributeError:
        print("Command should look like `cp file.txt file-copy.txt`.")
