def copy_file(files_name: str) -> None:
    command_line = files_name.split(" ")
    if len(command_line) == 3 and command_line[0] == "cp":
        command, name_old_file, name_new_file = command_line
        if name_old_file != name_new_file:
            with (open(name_new_file, "w") as new_file,
                  open(name_old_file, "r") as old_file):
                new_file.write(old_file.read())