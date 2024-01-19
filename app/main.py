def copy_file(command: str) -> None:
    if len(command) >= 3:
        cp, source, destination = command.split()
        if (
                cp == "cp"
                and source != destination
        ):
            with (
                open(source, "r") as file_in,
                open(destination, "w") as file_out
            ):
                file_out.write(file_in.read())
