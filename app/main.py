def copy_file(command: str):
    splitted_command = command.split("")
    with (open(splitted_command[1], "r") as f_original,
          open(splitted_command[2], "w") as f_copy):
        if splitted_command[1] == splitted_command[2]:
            pass
        else:
            f_copy.write(f_original.read())
