def copy_file(command: str = "cp file.txt file-copy.txt") -> None:
    command_name, old_file_name, new_file_name = command.split()
    if old_file_name != new_file_name and command_name == "cp":
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
