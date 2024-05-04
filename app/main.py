def copy_file(command_line: str) -> None:

    command, first_file, second_file  = command_line.split()

    if command == "cp":
        if first_file != second_file:
            with (open(first_file, "r") as file_in,
                  open(second_file, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
