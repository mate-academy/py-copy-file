import os


def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3 and command[0] == "cp":
        source, target = command[1], command[2]
        if os.path.exists(source):
            if source != target:
                with (open(source, "r") as file_in,
                      open(target, "w") as file_out):
                    for line in file_in:
                        file_out.write(line)
