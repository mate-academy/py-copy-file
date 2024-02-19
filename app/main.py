def copy_file(command: str) -> None:
    ls_of_command = command.split()
    if ls_of_command[0] == "cp":
        if ls_of_command[1] != ls_of_command[2]:
            with (open(ls_of_command[1], "r") as file,
                  open(ls_of_command[2], "w") as new_file):
                new_file.write(file.read())
