def copy_file(command: str) -> None:
    command_split = command.split(" ")

    if len(command_split) != 3 or command_split[0] != "cp":
        return

    elif command_split[1] == command_split[2]:
        return

    try:
        with (
            open(command_split[1], "r") as file_in,
            open(command_split[2], "w") as file_out,
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
