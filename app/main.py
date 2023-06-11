from os import path


def copy_file(command: str) -> None:
    try:
        cmd, file_to_copy, new_file = command.split()

        if cmd != "cp":
            raise ValueError(
                "Wrong command! You should use 'cp' to copy your file."
            )
        if file_to_copy == new_file:
            raise ValueError(
                "Wrong new file name! You can't copy file to itself!"
            )
        if not path.exists(file_to_copy):
            raise FileNotFoundError("Source file doesn't exist!")

        with (open(file_to_copy, "r") as input_file,
              open(new_file, "w") as output_file):
            output_file.write(input_file.read())

    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
