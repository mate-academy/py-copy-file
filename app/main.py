def copy_file(command: str) -> None:
    commands = command.split()
    if (
        len(commands) < 3 or
        commands[0] != "cp" or
        commands[1] == commands[2]
    ):
        return
    try:
        with open(commands[1], "r") as source, open(commands[2], "a") as target:
            for line in source:
                target.write(line)
    except UnicodeError:
        print("Error while copy file")

if __name__ == "__main__":
    copy_file(input("Input command: "))
