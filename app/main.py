def copy_file(command: str) -> None:
    cp_command = command.split()
    if cp_command[1] != cp_command[2]:
        with (open(cp_command[1], "r") as file,
              open(cp_command[2], "w") as new_file):
            content = file.read()
            new_file.write(content)
