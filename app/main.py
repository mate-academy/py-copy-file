def copy_file(command: str) -> None:
    separate_command = command.split()
    if len(separate_command) >= 3 and separate_command[0] == "cp":
        in_file_name = separate_command[1]
        out_file_name = separate_command[2]
    else:
        return "Incorrect command!"

    if in_file_name == out_file_name:
        return

    with (open(in_file_name, "r") as file_in,
            open(out_file_name, "w") as file_out):
        file_out.write(file_in.read())
