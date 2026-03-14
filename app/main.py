from pathlib import Path


def copy_file(
    command: str
) -> None:
    cmd_file1_file2 = command.split()
    if len(cmd_file1_file2) == 3 and cmd_file1_file2[0] == "cp":
        file_1 = Path(cmd_file1_file2[1])
        file_2 = Path(cmd_file1_file2[2])
    else:
        return
    if file_1 != file_2 and file_1.exists():
        with open(file_1, "r") as origin, open(file_2, "w") as copy:
            for line in origin:
                copy.write(line)
