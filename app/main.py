import os


def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return
    cmd = command.split(" ")
    if len(cmd) != 3:
        return
    cmd, file_1, file_2 = cmd
    if file_1 == file_2:
        return
    if not os.path.exists(file_1):
        return
    with open(file_1, "r") as f_in, open(file_2, "w") as f_out:
        f_out.write(f_in.read())
