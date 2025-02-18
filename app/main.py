def copy_file(command: str) -> None:
    line = command.split()

    if line[0] != "cp":
        raise ValueError("Bad command")

    source_file = line[1]
    destination_file = line[2]

    if source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
