from typing import Optional


def copy_file(command: str) -> Optional[str]:

    original_file = command.split(" ")[1]
    copied_file = command.split(" ")[2]

    if original_file == copied_file:
        return

    with (open(original_file, "r") as file_in,
          open(copied_file, "w") as file_out):
        file_out.write(file_in.read())

    return copied_file
