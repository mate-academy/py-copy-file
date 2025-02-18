def copy_file(command: str) -> None:
    splitted_command = command.split(" ")
    if splitted_command[0] == "cp" and len(splitted_command) == 3:
        with (open(splitted_command[1], "r") as current_file,
              open(splitted_command[2], "w+") as new):
            content = current_file.read()
            new.write(content)
