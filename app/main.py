import os


def copy_file(command: str) -> None:
    if len(command_chain := command.split(" ")) != 3:
        return
    command, source, destination = command_chain
    if (
        command == "cp"
        and os.path.exists(source)
        and source != destination
    ):
        with (
            open(source, "r") as file_in,
            open(destination, "w") as file_out
        ):
            file_out.write(file_in.read())
