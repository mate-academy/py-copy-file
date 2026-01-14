import os


def copy_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3 and ls[0] == "cp":
        source_file = ls[1]
        destination_file = ls[2]
        if os.path.exists(source_file):
            if source_file != destination_file:
                with (open(f"{source_file}", "r") as f,
                      open(f"{destination_file}", "w") as nf):
                    nf.write(f.read())
