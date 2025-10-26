import os


def copy_file(command: str) -> None:
    command = command.split()
    if command:
        if (command[0] == "cp" and len(command) == 3
                and command[1] != command[2]):
            file_to_copy = command[1]
            new_file = command[2]
            if not os.path.exists(file_to_copy):
                return
            with (open(file_to_copy, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
