def copy_file(command: str) -> None:
    command = command.split(" ")

    if (command[1] != command[2]) and command[0] == "cp":
        with (open(command[1], "r") as old_file,
              open(command[2], "w") as new_file):
            content = old_file.read()
            new_file.write(content)
