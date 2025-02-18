def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[1] != parts[2] and parts[0] == "cp":
        with (open(parts[1], "r") as source,
              open(parts[2], "w") as destination):
            destination.write(source.read())
