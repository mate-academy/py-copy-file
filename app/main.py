def copy_file(command: str) -> None:
    separate = command.split()
    if len(separate) != 3 or separate[0] != "cp":
        raise StopIteration
    with (open(separate[1], "r") as source_file,
          open(separate[2], "w") as destination_file):
        if separate[1] == separate[2]:
            pass
        else:
            for item in source_file:
                destination_file.write(item)
