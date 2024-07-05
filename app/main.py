import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command format.")
    else:
        source_file, destination_file = parts[1:]

        if source_file != destination_file:
            with (open(source_file, "rb") as fin,
                  open(destination_file, "wb") as fout):
                shutil.copyfileobj(fin, fout)
