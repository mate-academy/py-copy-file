def copy_file(command: str) -> None:
    args_list = command.split()
    if len(args_list) != 3 or args_list[0] != "cp":
        return
    source, destination = args_list[1:]
    if source == destination:
        return
    with open(source, "r") as source_file,\
         open(destination, "w") as destination_file:
        destination_file.write(source_file.read())
