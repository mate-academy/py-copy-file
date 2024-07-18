from typing import Any


def copy_file(command: str) -> Any:
    if len(command.split()) != 3 or command.split()[0] != "cp":
        print("Invalid command format."
              " Use: cp <source_file> <destination_file>")
        return

    cp, old_file, new_file = command.split()

    if old_file == new_file:
        print("Source and destination files are the same. No action taken.")
        return
    elif old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            lines = file_in.read()
            file_out.write(lines)
