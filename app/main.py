def copy_file(command: str) -> None:
    command_to_ls = command.split(", ")
    if command_to_ls[0] == "cp" and command_to_ls[1] != command_to_ls[2]:
        with (open(command_to_ls[1], "r") as file_in,
              open(command_to_ls[2], "w") as file_out):
            file_out.write(file_in.read())
