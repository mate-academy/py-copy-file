def copy_file(command: str) -> None:
    split_command = command.split()
    with (open(split_command[1], "r") as file_in,
          open(split_command[2], "w") as file_out):
        file_out.write(file_in.read())
