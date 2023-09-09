def copy_file(command: str) -> None:
    if command.startswith("cp"):
        split_command = command.split()
        with open(split_command[1], "r") as file_in,\
             open(split_command[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
