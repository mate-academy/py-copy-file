def copy_file(cp: str) -> None:
    parts = cp.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        raise Exception
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return
    with (open(source, "r") as file_in,
          open(destination, "w") as file_out):
        file_out.write(file_in.read())
