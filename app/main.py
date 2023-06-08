from os import path
import sys


def copy_file(command: str) -> str or None:
    cmd, main_file, new_file = command.split()
    source = path.join(sys.path[0], main_file)
    destination = path.join(sys.path[0], new_file)
    try:
        if cmd != "cp":
            raise ValueError("Wrong command! You should use `cp`.")
        if main_file == new_file:
            raise ValueError("Cannot copy file to itself!")

    # we can use copy() from shutil, but I've made it in more "vanilla" way
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except ValueError as e:
        print(f"ValueError: {e}")
    else:
        print("File copied successfully!")
