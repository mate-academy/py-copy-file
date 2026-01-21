def copy_file(command: str) -> None:

    command_list = command.split(" ")

    if len(command_list) != 3:
        return
    if command_list[0] != "cp":
        return
    source_file_name = command_list[1]
    destination_file_name = command_list[2]
    if source_file_name == destination_file_name:
        return
    try:
        with (open(source_file_name) as file_in,
              open(destination_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
