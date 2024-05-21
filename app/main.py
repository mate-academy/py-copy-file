def copy_file(command: str) -> None:
    command_split = command.split(" ")
    command_old = command_split[1]
    command_new = command_split[2]

    if command_new == command_old:
        exit()

    with (open(command_old, "r") as old_file,
          open(command_new, "w") as new_file):
        content = old_file.read()
        new_file.write(content)
