from typing import Any


def copy_file(command: str) -> Any:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use:"
              " cp <source_file> <destination_file>")
        return

    _, old_file, new_file = parts

    if old_file == new_file:
        print("Source and destination files"
              " are the same. No action taken.")
        return
    elif old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            lines = file_in.read()
            file_out.write(lines)
