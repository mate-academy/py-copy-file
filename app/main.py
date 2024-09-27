def copy_file(command: str) -> None:
    command_copy, origin, copy = command.split()

    if origin != copy and command_copy == "cp":

        with (
            open(origin, "r") as origin,
            open(copy, "w") as copy
        ):
            copy.write(origin.read())
