def copy_file(command: str) -> None:
    splitted_command = command.split()
    original_file = splitted_command[1]
    copy = splitted_command[2]
    cp_command_check = splitted_command[0]

    if not cp_command_check == "cp":
        return

    if original_file == copy_file:
        return

    with (open(original_file, "r") as f_original,
          open(copy, "w") as f_copy):
        f_copy.write(f_original.read())
