from os import path


def copy_file(command: str) -> str or None:

    try:
        cmd, main_file, new_file = command.split()

        if cmd != "cp":
            raise ValueError("Wrong command! You should use `cp`.")
        if main_file == new_file:
            raise ValueError("Cannot copy file to itself!")
        if not path.exists(main_file):
            raise FileNotFoundError("Source file doesn't exist!")

        with open(main_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())

        print("File copied successfully!")

    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
