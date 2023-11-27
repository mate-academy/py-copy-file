def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if split_command[1] != split_command[2]:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            content = file_in.read()
            file_out.write(content)
