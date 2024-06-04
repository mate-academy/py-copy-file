def copy_file(command: str) -> None:
    command_list = command.split()
    from_file = command_list[1]
    to_file = command_list[2]
    if "cp" in command_list or from_file != to_file or len(command_list) != 3:
        return
    with (open(f"{from_file}", "r") as file,
          open(f"{to_file}", "w") as new_file):
        new_file.write(f"{file.read()}")
