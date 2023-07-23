import shutil


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        raise ValueError("Invalid command format")

    _, source_file, destination_file = command_parts

    if source_file == destination_file:
        return

    with open(source_file, "r") as file_in, \
            open(destination_file, "w") as file_out:
        shutil.copyfileobj(file_in, file_out)
