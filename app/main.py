def copy_file(command: str) -> None:
    element = command.split(" ")
    if element[1] != element[2]:
        with (open(element[1], "r") as source_file,
              open(element[2], "w") as destination_file):
            for line in source_file:
                destination_file.write(line)
