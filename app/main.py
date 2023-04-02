def copy_file(command: str) -> None:
    splitted_command = command.split()
    old_file_name = splitted_command[1]
    new_file_name = splitted_command[2]
    if old_file_name != new_file_name:
        with (open(old_file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
