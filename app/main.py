import os.path


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        if parts[0] == "cp":
            if parts[1] == parts[2]:
                return
            if not os.path.exists(parts[1]):
                return
            with (
                open(parts[1], "r") as file_in,
                open(parts[2], "w") as file_out
            ):
                file_out.write(file_in.read())
