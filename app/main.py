def copy_file(command: str) -> None:
    sep_command = command.split()

    with open(sep_command[1], "r") as f, open(sep_command[-1], "w") as w:
        w.write(f.read())
