import os


def copy_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        cp_command, initial_file, copied_file = elements
        if cp_command == "cp" and initial_file != copied_file:
            with (
                open(initial_file, "r") as file_in,
                open(copied_file, "w") as file_out
            ):
                if os.path.exists(initial_file):
                    file_out.write(file_in.read())
