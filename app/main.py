import os


def copy_file(command: str) -> None:
    command = command.split()
    if len(command) < 3:
        return
    command, file_in, file_out = command[0], command[1], command[2]
    if file_in == file_out:
        return
    if os.path.exists(file_in):
        if command == "cp":
            with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
                f_out.write(f_in.read())
