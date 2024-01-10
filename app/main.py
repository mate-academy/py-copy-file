def copy_file(command: str) -> None:
    ls_command = command.split(" ")
    if ls_command[1] != ls_command[2] and ls_command[0] == "cp":
        with (open(ls_command[1], "r") as source,
              open(ls_command[2], "w") as new_file):
            new_file.write(source.read())
