def copy_file(command: str) -> None:
    command_type, copy_from, copy_to, *_ = command.split()
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
