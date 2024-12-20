from typing import Optional


def copy_file(command: str) -> Optional[str]:
    command_info = command.split()

    if command_info[0] == "cp":
        source, destination = command_info[1], command_info[2]

        if source == destination:
            return None

        with (open(source, "r") as original_file,
              open(destination, "w") as new_file):
            new_file.write(original_file.read())
