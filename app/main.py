def copy_file(command: str) -> any:
    if (len(command.split(" ")) != 3
            or command.split(" ")[0] != "cp"):
        return
    source = command.split(" ")[1]
    destination = command.split(" ")[2]
    try:
        if source != destination:
            with (open(source, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
        else:
            return
    except FileNotFoundError:
        return
