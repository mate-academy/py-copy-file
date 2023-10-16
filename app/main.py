def copy_file(command: str) -> None:
    command = command.split()
    path_origin = command[1]
    path_copy = command[2]

    if path_origin != path_copy:
        with (open(path_origin, "r") as file_in,
              open(path_copy, "w") as file_out):
            file_out.write(file_in.read())
