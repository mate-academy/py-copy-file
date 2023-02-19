def copy_file(command: str) -> None:
    commands_list = command.split()
    if commands_list[0] == "cp" and commands_list[1] != commands_list[2]:
        with open(commands_list[1], "r") as file_in, open(
            commands_list[2], "w"
        ) as file_out:
            file_out.write(file_in.read())
