import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination_file = parts[2]

    if source_file != destination_file:
        with (open(source_file, "rb") as fin,
              open(destination_file, "wb") as fout):
            shutil.copyfileobj(fin, fout)
