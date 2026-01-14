import os


def copy_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3 and ls[0] == "cp":
        file_name = ls[1]
        new_file_name = ls[2]
        if os.path.exists(file_name):
            if file_name != new_file_name:
                with (open(f"{file_name}", "r") as f,
                      open(f"{new_file_name}", "w") as nf):
                    nf.write(f.read())
