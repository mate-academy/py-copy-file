from typing import Any


def copy_file(command: str) -> Any:
    try:
        command_split = command.split(" ")

        if command_split[0] != "cp":
            return

        source_name = command_split[1]
        destination_name = command_split[2]

        if source_name == destination_name:
            return

        with (open(source_name, "r") as file_in,
              open(destination_name, "w") as file_out):

            file_out.write(file_in.read())
    except Exception as e:
        print(e)
