def copy_file(command_patch: str) -> None:
    command, first_file_name, second_file_name = command_patch.split()

    if command == "cp":
        with (
            open(first_file_name, "w") as file_in,
            open(second_file_name, "r") as file_out
        ):
            if first_file_name != second_file_name:
                file_in.write(file_out.read())
