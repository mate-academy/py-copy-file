def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) < 3:
        return
    if commands[0] != "cp":
        return
    if commands[1] == commands[2]:
        return

    with open(commands[1], "r") as source, open(commands[2], "w") as target:
        source.write(target.read())


if __name__ == "__main__":
    copy_file(input("Input command: "))
