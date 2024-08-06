def copy_file(command: str) -> None:
    command, first_name, second_name = command.split()

    if first_name != second_name and command == "cp":
        with open(first_name) as file_in, open(second_name, "w") as file_out:
            file_out.write(file_in.read())
