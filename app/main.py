def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) != 3:
        return
    cp, source_file_name, destination_file_name = split_command

    if cp != "cp":
        return
    elif source_file_name == destination_file_name:
        return
    else:
        try:
            with (open(source_file_name, "r") as original,
                  open(destination_file_name, "w") as copy):
                copy.write(original.read())
        except FileNotFoundError:
            pass
