def copy_file(command: str) -> None:
    command = command.split(" ")
    path_in = command[1]
    path_out = command[2]
    if path_in != path_out:
        with open(path_in, "r") as file_in, open(path_out, "w") as file_out:
            file_in.write(file_out.read())
