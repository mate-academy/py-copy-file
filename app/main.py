def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3:
        raise ValueError
    if split_command[0] != "cp":
        raise ValueError
    if split_command[1] == split_command[2]:
        raise ValueError

    _, input_file, output_file = split_command
    with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
        f_out.write(f_in.read())
