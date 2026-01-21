
def copy_file(command: str) -> None:
    split_command = command.split()
    if (len(split_command) == 3
            and split_command[0] == "cp"
            and split_command[1] != split_command[2]):

        try:
            with (open(split_command[1], "r") as copy_from_file,
                  open(split_command[2], "w") as copy_to_file):
                copy_to_file.write(copy_from_file.read())
        except FileNotFoundError:
            pass
