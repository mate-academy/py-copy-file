def copy_file(command: str) -> None:
    command_info = command.split()
    if command_info[1] != command_info[2]:
        with (open(command_info[1], "r") as origin_file,
              open(command_info[2], "w") as copied_file):
            copied_file.write(origin_file.read())
