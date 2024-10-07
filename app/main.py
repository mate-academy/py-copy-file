def copy_file(command: str) -> None:
    com_split = command.split()
    with (open(com_split[1], "r") as file_in,
          open(com_split[2], "w") as file_out):
        file_out.write(file_in.read())
