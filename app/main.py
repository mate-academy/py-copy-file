def copy_file(command_line: str) -> None:

    command_list = command_line.split()
    command = command_list[0]
    first_file = command_list[1]
    second_file = command_list[2]

    if command == "cp":
        if first_file != second_file:
            with (open(first_file, "r") as file_in,
                  open(second_file, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
