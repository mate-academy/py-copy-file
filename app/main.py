import shutil
import os


def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source, destination = parts[1], parts[2]
    if source == destination:
        return  # Do nothing if source and destination are the same

    if not os.path.isfile(source):
        return

    with (open(source, "r", encoding="utf-8") as file_in,
          open(destination, "w", encoding="utf-8") as file_out):
        shutil.copyfileobj(file_in, file_out)
