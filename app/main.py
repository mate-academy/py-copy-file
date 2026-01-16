from _pyrepl import commands


def copy_file(command) -> None:
    cp, src, dst = command.split()
    command_split = command.split()

    for c in command_split:
        if c == 3:
            return
        elif c != "cp":
            return

    if src == dst:
        return

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())