import os
from typing import List


def copy_file(command: str) -> None:
    parts: List[str] = command.split()

    # Sprawdzamy czy komenda ma 3 części i czy zaczyna się od cp
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_file, target_file = parts

    # Nic nie robimy, jeśli nazwy są takie same
    if source_file == target_file:
        return

    # Sprawdzamy czy plik źródłowy w ogóle istnieje
    if not os.path.exists(source_file):
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
