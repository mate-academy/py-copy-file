import os


def copy_file(command: str) -> None:
    parts_of_command = command.split()
    if len(parts_of_command) != 3:
        return
    elif parts_of_command[0] != "cp":
        return
    elif parts_of_command[1] == parts_of_command[2]:
        return
    elif not os.path.isfile(parts_of_command[1]):
        return

    with (
        open(parts_of_command[1], "r") as file_in,
        open(parts_of_command[2], "w") as file_out
    ):
        for line in file_in:
            file_out.write(line)
