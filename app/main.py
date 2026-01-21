def copy_file(command: str) -> None:
    list_of_command = command.split(" ")
    if len(list_of_command) == 3:
        if (
            list_of_command[0] == "cp"
            and list_of_command[1] != list_of_command[2]
        ):
            with (
                open(list_of_command[1], "r") as f_in,
                open(list_of_command[2], "w") as f_out
            ):
                f_out.write(f_in.read())
