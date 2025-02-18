def copy_file(command: str) -> None:
    split_command = command.split()
    if (len(split_command) == 3
            and split_command[1] != split_command[2]
            and split_command[0] == "cp"):
        with (open(split_command[1], "r") as origin,
              open(split_command[2], "w") as copy):
            copy.write(origin.read())
