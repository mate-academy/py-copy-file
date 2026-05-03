def copy_file(command: str) -> None:
    command_part = command.split()
    if len(command_part) < 3 or command_part[0] != "cp":
        return
    source = command_part[1]
    destination = command_part[2]
    try:
        if source != destination:
            with (open(source, "r") as file_in,
                  open(destination, "w") as file_out):
                content_file = file_in.read()
                file_out.write(content_file)
    except FileNotFoundError:
        pass
