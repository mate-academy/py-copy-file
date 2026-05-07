from pathlib import Path


def copy_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return

    cm, f1, f2 = arguments
    f1_path, f2_path = Path(f1), Path(f2)
    if cm != "cp":
        return

    if not f1_path.is_file():
        return

    if f2_path.exists() and f1_path.samefile(f2_path):
        return

    with open(f1_path, "r", encoding="utf-8") as file_in, \
            open(f2_path, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
