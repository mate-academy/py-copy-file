def copy_file(command: str) -> None:
    list_comands = command.split()

    if len(list_comands) != 3:
        return

    action, source_file, destination_file = list_comands

    if action != "cp":
        return

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
