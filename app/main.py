def copy_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3 and ls[0] == "cp":
        source_file = ls[1]
        destination_file = ls[2]
        if not source_file == destination_file:
            with (open(source_file, "r") as source,
                  open(destination_file, "w") as destination):
                destination.write(source.read())
