def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("some informative message")
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        print("some informative message")
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
