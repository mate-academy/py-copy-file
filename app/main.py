def copy_file(command: str) -> None:

    if (len(command.split()) != 3 and command.split()[0] != "cp"
            and command.count(" ") != 2):
        return
    command_parts = command.split()

    with (open(command_parts[1], "r") as file_in,
          open(command_parts[2], "w") as file_out):
        if command_parts[1] == command_parts[2]:
            return
        for line in file_in:
            file_out.write(line)
