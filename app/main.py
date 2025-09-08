from pathlib import Path


def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) != 3:
        return

    if command_list[1] == command_list[2]:
        return

    if command_list[0] == "cp":

        source_file_name = command_list[1]
        destination_file_name = command_list[2]

        if not Path(source_file_name).is_file():
            return

        with (open(source_file_name, "r") as file_in,
              open(destination_file_name, "w") as file_out):
            file_out.write(file_in.read())
