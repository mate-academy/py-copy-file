def copy_file(command: str) -> None:
    sort_command = command.split()
    if sort_command[0] == "cp" and sort_command[1] != sort_command[2]:
        with (open(sort_command[1], "r") as file_in,
              open(sort_command[2], "w") as file_out):
            file_out.write(file_in.read())
