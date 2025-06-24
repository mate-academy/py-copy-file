def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "cp" and len(command_list) == 3:
        if command_list[1] != command_list[2]:
            try:
                with (open(command_list[1], "r") as file_from,
                      open(command_list[2], "w") as file_to):
                    for line in file_from:
                        file_to.write(line)
            except FileNotFoundError:
                print(f"File not found: {command_list[1]}")
            except Exception as e:
                print(f"An error occurred: {e}")
