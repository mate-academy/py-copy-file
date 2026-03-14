import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cmd, source_filename, destination_filename = parts

    if cmd != "cp":
        return

    if source_filename == destination_filename:
        return

    if not os.path.exists(source_filename):
        return

    with (open(source_filename, "r") as source_file,
          open(destination_filename, "w") as destination_file):
        destination_file.write(source_file.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
