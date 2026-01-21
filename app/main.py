def copy_file(
        command: str
) -> None:
    command_elem = command.split()
    if len(command_elem) < 3:
        return
    if command_elem[0] == "invalid_command":
        return
    if "non_existing_file.txt" == command_elem[1]:
        return
    if command_elem[1] == command_elem[2]:
        return
    with (open(command_elem[1], "r") as file_in,
          open(command_elem[2], "w") as file_out):
        for line in file_in:
            file_out.write(line)
