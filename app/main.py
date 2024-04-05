def copy_file(command: str) -> None:
    cp_command, file_for_copy, new_file = command.split()

    if cp_command != "cp":
        return

    if file_for_copy != new_file:
        with open(file_for_copy, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
