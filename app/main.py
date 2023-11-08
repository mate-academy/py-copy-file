def copy_file(command: str) -> None:

    sep_command = command.split()
    if not (len(sep_command) == 3):
        return
    cop, file_name, new_file_name = sep_command
    if file_name == new_file_name:
        return
    try:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
