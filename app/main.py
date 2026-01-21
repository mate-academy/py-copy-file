import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, destination_file = parts[1], parts[2]
    if parts[1] == parts[2]:
        return

    if not os.path.exists(source_file):
        return

    try:
        with (open(source_file, "r") as file1,
              open(destination_file, "w") as file2
              ):
            file2.write(file1.read())
    except Exception:
        pass

    file1.close()
    file2.close()
