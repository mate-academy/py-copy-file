def copy_file(command: str) -> None:
    one_command = command.split()
    try:
        if len(one_command) == 3:
            if ("cp" in one_command[0]
                    and one_command[1] != one_command[2]):

                with (open(one_command[1], "r") as file,
                      open(one_command[2], "w") as new_file):

                    new_file.write(file.read())
    except FileNotFoundError:
        return
