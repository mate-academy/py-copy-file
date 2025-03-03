import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    copied_file, new_file = parts[1], parts[2]
    if parts[1] == parts[2]:
        return

    if not os.path.exists(copied_file):
        return

    file1 = open(copied_file, "r")
    file2 = open(new_file, "w")
    try:
        file2.write(file1.read())
    except Exception:
        pass

    file1.close()
    file2.close()
