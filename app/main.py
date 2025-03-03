from typing import Any


def copy_file(command: str) -> Any:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Not correct command format. Use 'cp <file> <new_file>'")
        return
    file, new_file = parts[1], parts[2]

    if file == new_file:
        return

    try:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{file}' copied to '{new_file}'")

    except FileNotFoundError:
        print(f"Error: '{file}' not found.")
