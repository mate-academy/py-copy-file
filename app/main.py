import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            shutil.copyfileobj(file_in, file_out)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{source_file}' not found")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")
