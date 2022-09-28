def copy_file(command: str) -> None:
    params = command.split()
    with open(params[1], "r") as file_in, open(params[2], "w") as file_out:
        file_out.write(file_in.read())
