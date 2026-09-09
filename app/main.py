from pathlib import Path


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        file_path = Path(parts[1])
        file1, file2 = parts[1], parts[2]
        if file1 != file2 and file_path.is_file():
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                file_out.write(file_in.read())
