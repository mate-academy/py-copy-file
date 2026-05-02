def copy_file(command: str = "cp") -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return
    else:
        try:
            with open(source, "r") as f_in, open(destination, "w") as f_out:
                f_out.write(f_in.read())
        except FileNotFoundError:
            return
