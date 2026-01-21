import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    func, source, target = parts

    if (
            not source
            or not target
            or func != "cp"
            or source == target
            or not os.path.exists(source)
    ):
        return

    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
