def copy_file(command: str) -> None:
    command_splitted = command.split(" ")
    if len(command_splitted) != 3:
        print("Invalid length of arguments")
        return
    try:
        if command_splitted[0] == "cp":
            if command_splitted[1] != command_splitted[2]:
                with (open(command_splitted[1], "r") as file_from,
                      open(command_splitted[2], "w") as file_to):
                    file_to.write(file_from.read())
    except Exception as e:
        print(e)
