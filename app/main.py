import os


def copy_file(command: str) -> None:
    try:
        cp, current_file, copied_file = command.split()
    except ValueError:
        raise ValueError("Command is incorrect")
    if cp != "cp" or os.path.exists(current_file) is False:
        raise ValueError("Command is incorrect")
    if current_file != copied_file:
        with open(current_file,
                  "r") as file_in, open(copied_file, "w") as file_out:
            file_out.write(file_in.read())
