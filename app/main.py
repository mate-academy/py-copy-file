def copy_file(command: str) -> None:
    command_name, first_file, second_file = command.split()

    if first_file != second_file and command_name == "cp":
        with open(first_file, "r") as file_in, open(
            second_file, "w"
        ) as file_out:
            file_out.write(file_in.read())
