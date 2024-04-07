def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3:
        return

    if command[0] != "cp":
        return
    if command[1] == command[2]:
        return

    with (
        open(command[1], "r") as file1,
        open(command[2], "w") as file2
    ):
        file2.write(file1.read())
