import os


def copy_file(command: str) -> None:
    args = command.split()
    if len(args) != 3:
        return

    source_file, target_file = args[1], args[2]

    if source_file == target_file:
        return

    if not os.path.exists(source_file):
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
