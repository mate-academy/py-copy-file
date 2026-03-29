import os


def copy_file(command: str) -> None:
    command_files = command.split()
    if len(command_files) == 3 and command_files[0] == "cp":
        src, dst = command_files[1], command_files[2]
        if src == dst:
            return
        if not os.path.exists(src):
            return
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
