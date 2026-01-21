def copy_file(command: str) -> None:
    command, path_in, path_out = command.split()
    if command == "cp" and path_in != path_out:
        with (open(path_in, "r") as file_in,
              open(path_out, "w") as file_out):
            file_out.write(file_in.read())
