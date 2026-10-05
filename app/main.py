from pathlib import Path
import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, source_name, destination_name = parts
    source = Path(source_name)
    destination = Path(destination_name)
    if source.resolve() == destination.resolve() or not source.is_file():
        return
    if destination.exists() and source.samefile(destination):
        return
    with source.open("rb") as original, destination.open("wb") as copied:
        shutil.copyfileobj(original, copied)
