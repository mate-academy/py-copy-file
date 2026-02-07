import os


def copy_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) == 3 and parts_of_command[0] == "cp":
        (instruction, file_in, file_out) = parts_of_command

        if os.path.exists(file_in):
            with open(file_in, "r") as file1, open(file_out, "w") as file2:
                file2.write(file1.read())
