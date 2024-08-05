import shutil


def copy_file(command: str) -> None:
    action, src_file, dest_file = command.split()
    if action != "cp" or src_file == dest_file:
        raise ValueError("Invalid command format or source and destination files are the same")

    try:
        with (
            open(src_file, "r") as file_in,
            open(dest_file, "w") as file_out
        ):
            shutil.copyfileobj(file_in, file_out)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{src_file}' not found")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")
