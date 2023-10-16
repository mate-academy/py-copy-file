def copy_file(command: str) -> str:
    command_part = command.split()
    command = command_part[0]
    path_origin = command_part[1]
    path_copy = command_part[2]

    if path_origin != path_copy and command == "cp":
        with (open(path_origin, "r") as file_in,
              open(path_copy, "w") as file_out):
            file_out.write(file_in.read())

    else:
        return "Does nothing"
