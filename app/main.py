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
        print(f"Warning: Source file '{source}'"
              f" does not exist. No action taken.")
        return

    destination = os.path.join(os.getcwd(), destination)
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    with (open(source, "r", encoding="utf-8") as file_in,
          open(destination, "w", encoding="utf-8") as file_out):
        shutil.copyfileobj(file_in, file_out)

    print(f"File copied successfully to '{destination}'")
