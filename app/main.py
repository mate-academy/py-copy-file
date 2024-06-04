def copy_file(command: str) -> None:
    commands_list = command.split()
    if commands_list[0] == "cp":
        if commands_list[1] != commands_list[2]:
            with (open(commands_list[1], "r") as source_file,
                  open(commands_list[2], "w") as output_file):
                output_file.write(source_file.read())
