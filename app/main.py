def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    import os
    if not os.path.exists(parts[1]):
        return

    if parts[1] == parts[2]:
        return

    with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
