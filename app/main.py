def copy_file(command: str) -> None:
    split_command = command.split()
    command, current_file, new_file = split_command
    if (current_file != new_file
            and command == "cp" and len(split_command) == 3):
        with (open(current_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
