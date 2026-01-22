def copy_file(command: str) -> None:
    command_parts = command.strip().split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return
    origin_file, copied_file = command_parts[1], command_parts[2]
    if origin_file == copied_file:
        return
    try:
        with (open(origin_file, "r") as file_in,
              open(copied_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError as e:
        print(e)
