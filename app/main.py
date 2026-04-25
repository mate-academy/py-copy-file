def copy_file(command: str) -> None:
    try:
        incoming_command = command.split(" ")
        if (incoming_command[0] == "cp"
                and incoming_command[1] != incoming_command[2]):
            with (open(incoming_command[1], "r") as file_in,
                  open(incoming_command[2], "w") as file_out):
                file_out.write(file_in.read())

    except (FileNotFoundError, IndexError):
        pass
