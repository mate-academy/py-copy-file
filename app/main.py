def copy_file(command: str) -> None:
    split_command = command.split()
    first_part = split_command[1]
    second_part = split_command[2]

    if len(split_command) != 3 or split_command[0] != "cp":
        return
    if first_part == second_part:
        return

    with open(first_part, "r") as file_in, open(second_part, "w") as file_out:
        file_out.write(file_in.read())
