def copy_file(command: str) -> None:
    if command.count(" ") != 2:
        return
    command_parts = command.split(" ")
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return
    source_file_name = command_parts[1]
    target_file_name = command_parts[2]

    if source_file_name == target_file_name:
        return
    try:
        with (open(source_file_name, "r") as source_file_object,
              open(target_file_name, "w") as target_file_object):
            target_file_object.write(source_file_object.read())
    except FileNotFoundError:
        pass
