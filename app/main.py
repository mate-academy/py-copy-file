def copy_file(command: str) -> None:
    current_file = command.split()[1]
    new_file = command.split()[2]
    if current_file != new_file:
        with (open(current_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
