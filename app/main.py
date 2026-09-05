from pathlib import Path


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3:
        return

    if parts[0] != "cp":
        return

    file_name = parts[1]
    new_file_name = parts[2]

    if file_name == new_file_name:
        return

    file_path = Path(file_name)

    if file_path.is_file():
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            for line in file_in:
                file_out.write(line)
