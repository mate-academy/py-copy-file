def copy_file(command: str) -> str:
    command, path_origin, path_copy = command.split()

    if path_origin != path_copy and command == "cp":
        with (open(path_origin, "r") as file_in,
              open(path_copy, "w") as file_out):
            file_out.write(file_in.read())

    else:
        return "Does nothing"
