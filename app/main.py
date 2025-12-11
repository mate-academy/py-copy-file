def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "cp":
        source_file = split_command[1]
        copied_file = split_command[2]
        try:
            if source_file != copied_file:
                with (open(source_file, "r") as file_in,
                      open(copied_file, "w") as file_out):
                    file_out.write(file_in.read())
        except FileNotFoundError:
            pass
