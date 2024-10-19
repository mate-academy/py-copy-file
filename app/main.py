def copy_file(command: str) -> None:
    file_out = command.split()[1]
    file_in = command.split()[2]
    with (open(file_out) as file_out,
          open(file_in, "w") as file_in):
        file_in.write(file_out.read())
