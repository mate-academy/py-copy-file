import os.path


def copy_file(command: str) -> None:
    if command.split()[0] == "cp":
        if command.split()[1] != command.split()[2]:
            if os.path.exists(command.split()[1]):
                with open(command.split()[1], "r") as file_in,\
                        open(command.split()[2], "w") as file_out:
                    file_out.write(file_in.read())
