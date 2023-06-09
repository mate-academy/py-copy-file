from os import path, getcwd


def copy_file(command: str) -> str or None:

    try:
        cmd, main_file, new_file = command.split()
        source = fr"{getcwd()}\{main_file}"

        if cmd != "cp":
            raise ValueError("Wrong command! You should use `cp`.")
        if main_file == new_file:
            raise ValueError("Cannot copy file to itself!")
        if not (main_file.endswith(".txt") and new_file.endswith(".txt")):
            raise ValueError("Files are in wrong format!")
        if not path.exists(source):
            raise FileNotFoundError("Source file doesn't exist!")

        with open(source, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())

        print("File copied successfully!")

    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
