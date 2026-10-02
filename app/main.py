import os


def copy_file(command: str) -> None:
    command_data = command.split()

    if (
            len(command_data) < 3
            or command_data[0] != "cp"
            or command_data[1] == command_data[2]
            or not os.path.exists(command_data[1])
    ):
        return

    with (
        open(command_data[1], "r") as file_in,
        open(command_data[2], "w") as file_out
    ):
        file_out.write(file_in.read())
