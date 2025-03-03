import os


def copy_file(command: str) -> None:
    files = command.split()
    if "cp" not in files or len(files) != 3:
        return

    first_file = files[1]
    second_file = files[2]

    if first_file == second_file or not os.path.exists(first_file):
        return

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())
