def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "cp":
        first_file = split_command[1]
        another_file = split_command[-1]
        if first_file == another_file:
            return None

        with (open(first_file, "r") as file_in,
              open(another_file, "w") as file_out):

            file_out.write(file_in.read())
