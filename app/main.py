def copy_file(command: str) -> None:
    command = command.split()

    if command[1] != command[2]:

        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):

            file_out.write(file_in.read())
