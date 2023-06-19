from os import path


def copy_file(command: str) -> None:
    try:
        cmd, file_to_copy, new_file = command.split()
        if cmd != "cp":
            raise ValueError(
                "Wrong command, you should use 'cp' command to copy file"
            )
        if not path.exists(file_to_copy):
            raise FileNotFoundError("File doesn't exists")

        with open(file_to_copy, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
