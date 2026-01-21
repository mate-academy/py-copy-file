import os


def copy_file(command: str) -> None:
    params = command.split()

    if len(params) != 3:
        return
    cp, source, target = params
    if cp != "cp":
        return

    if not os.path.exists(source):
        return

    if source != target:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            for line in file_in:
                file_out.write(line)
