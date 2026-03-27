import os


def copy_file(command: str) -> None:
    try:
        cp, read_file, write_file = command.split()
    except ValueError:
        return
    if cp != "cp" or read_file == write_file:
        return
    if not os.path.isfile(read_file):
        return
    with open(read_file, "r") as file_in, open(write_file, "w") as file_out:
        reader = file_in.read()
        file_out.write(reader)
