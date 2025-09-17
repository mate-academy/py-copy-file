def copy_file(command : str) -> None:
    part = command.split(" ")
    if len(part) != 3 or part[0] != "cp":
        return
    source_file = part[1]
    destination_file = part[2]
    if source_file == destination_file:
        return
    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
