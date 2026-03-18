import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "cp":
        return

    file_name = parts[1]
    new_file_name = parts[2]

    if file_name == new_file_name or not os.path.exists(file_name):
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
