def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) != 3 or split_command[0] != "cp":
        return
    first_file, second_file = split_command[1], split_command[2]

    if first_file == second_file:
        return
    try:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            read_file = file_in.read()
            file_out.write(read_file)
    except FileNotFoundError:
        return
