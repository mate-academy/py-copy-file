def copy_file(command: str) -> None:
    comms = command.split(" ")
    try:
        if comms[0] == "cp" and comms[1] != comms[2] and len(comms) == 3:
            with (
                open(comms[1], "r") as file,
                open(comms[2], "w") as new_file
            ):
                new_file.write(file.read())
    except (FileNotFoundError, IndexError):
        pass
    return
