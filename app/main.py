def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    if split_command[1] == split_command[2]:
        return

    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            read_content = file_in.read()
            file_out.write(read_content)
    except FileNotFoundError:
        return
