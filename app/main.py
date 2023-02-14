def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command")
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return
    with(
        open(source, "r") as file_in,
        open(destination, "w") as file_out
    ):
        file_out.write(file_in.read())
