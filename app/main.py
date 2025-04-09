def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and "cp" in split_command:
        src, dest = split_command[1], split_command[2]
        if src != dest:
            try:
                with (open(src, "r") as file_in,
                      open(dest, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                pass
