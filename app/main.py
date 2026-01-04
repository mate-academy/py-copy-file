def copy_file(command: str) -> None:
    command, file, new_file = command.split()

    if command != "cp" or file == new_file:
        raise ValueError()

    with (open(file, "r") as file_in,
          open(new_file, "w") as file_out):
        file_out.write(file_in.read())
