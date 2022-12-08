import shutil


def copy_file(command: str) -> None:
    command = command.split()

    if command[1] != command[2] and command[0] == "cp":
        with (open(command[1], "r") as file_in,
              open(command[2], "a") as file_out):
            shutil.copyfile(file_in.name, file_out.name)
