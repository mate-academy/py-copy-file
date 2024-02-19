def copy_file(command: str) -> None:
    if (
            len(command.split()) == 3
            and command.split()[0] == "cp"
            and command.split()[1] != command.split()[2]
    ):

        with (open(command.split()[1], "r") as file,
              open(command.split()[2], "w") as new_file):
            new_file.write(file.read())
