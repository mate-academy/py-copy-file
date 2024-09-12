import os


def copy_file(command: str) -> None:
    try:
        input_command, current_file, copied_file = command.split()
    except ValueError:
        raise ValueError("Command is incorrect")
    if input_command != "cp" or not os.path.exists(current_file):
        raise ValueError("Command is incorrect")
    if current_file != copied_file:
        with (
            open(current_file, "r") as file_in,
            open(copied_file, "w") as file_out
        ):
            file_out.write(file_in.read())
