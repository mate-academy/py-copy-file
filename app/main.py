def copy_file(command: str) -> None:
    with (open(command.split()[1], "r") as file_in,
          open(command.split()[2], "w") as file_out):
        file_out.write(file_in.read())
