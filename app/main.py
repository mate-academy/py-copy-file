def copy_file(command: str) -> None:
    if command == "":
        return
    command_split = command.split(" ")
    if len(command_split) != 3:
        return
    if command_split[0] != "cp":
        return
    if command_split[1] == command_split[2]:
        return
    try:
        open(command_split[1], "r").close()
    except FileNotFoundError:
        return

    with (
        open(command_split[1], "r") as file_in,
        open(command_split[2], "w") as file_out
    ):
        file_out.write(file_in.read())
