import shutil


def copy_file(command: str) -> None:
    tokens = command.split()
    try:
        if (len(tokens) == 3
                and tokens[1] != tokens[2]
                and tokens[0] == "cp"):
            shutil.copy2(tokens[1], tokens[2])
    except FileNotFoundError:
        pass
