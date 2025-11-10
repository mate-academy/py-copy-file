import os


def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) != 3:
        return

    command_word, source, destination = parts

    if (
        not os.path.exists(source)
        or source == destination
        or command_word != "cp"
    ):
        return

    with (open(source, "r") as file_in,
          open(destination, "w") as file_out):
        file_out.write(file_in.read())
