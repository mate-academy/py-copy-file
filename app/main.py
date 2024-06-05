def copy_file(command: str) -> None:
    command_list = command.split()
    if ("cp" in command_list
            or command_list[1] != command_list[2]
            or len(command_list) != 3):
        return
    with (open(f"{command_list[1]}", "r") as file,
          open(f"{command_list[2]}", "w") as new_file):
        new_file.write(f"{file.read()}")
