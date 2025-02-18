def copy_file(cp_command: str) -> None:
    splitted_cp_command = cp_command.split()
    if (
        len(splitted_cp_command) == 3
        and splitted_cp_command[0] == "cp"
        and splitted_cp_command[1] != splitted_cp_command[2]
    ):
        with (
            open(splitted_cp_command[1], "r") as file_in,
            open(splitted_cp_command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
