def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3:
        command_type, copy_from, copy_to = command_split

        if copy_from == copy_to:
            return

        if command_type == "cp":
            with (
                open(copy_from, "r") as starting_file,
                open(copy_to, "w") as destination_file
            ):
                destination_file.write(
                    starting_file.read()
                )
