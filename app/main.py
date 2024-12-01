def copy_file(command: str) -> None:
    check_command = command.split()
    if (len(check_command) != 3 or
            check_command[0] != "cp" or
            check_command[1] == check_command[2]):
        return
    with (open(check_command[1], "r") as file_in,
          open(check_command[2], "w") as file_out):
        for line in file_in:
            file_out.write(line + "\n")
