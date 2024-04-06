def copy_file(command: str) -> None:
    command = command.split()
    with (
        open(command[1], "r") as f1,
        open(command[2], "w") as f2
    ):
        f2.write(f1.read())
