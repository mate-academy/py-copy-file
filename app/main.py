def copy_file(command: str) -> None:
    command_splitted = command.split(" ")
    try:
        if command_splitted[0] == "cp":
            if command_splitted[1] and command_splitted[2]:
                if command_splitted[1] != command_splitted[2]:
                    with (open(command_splitted[1], "r") as file_from,
                          open(command_splitted[2], "w") as file_to):
                        file_to.write(file_from.read())
    except Exception:
        print(f"{Exception}")
