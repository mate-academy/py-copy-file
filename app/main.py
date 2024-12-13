def copy_file(command: str) -> None:
    _, file_name, new_name = command.split()
    try:
        with open(file_name, "r") as file_in, open(new_name, "x") as file_out:
            file_out.write(file_in.read())
    except FileExistsError:
        pass
