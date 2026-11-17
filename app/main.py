def copy_file(command: str) -> None:
    new_command = command.split()
    if (
        len(new_command) == 3
        and new_command[1] != new_command[2]
        and new_command[0] == "cp"
    ):
        try:
            with (
                open(f"{new_command[1]}", "r") as file_in,
                open(f"{new_command[2]}", "w") as file_out,
            ):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            pass
