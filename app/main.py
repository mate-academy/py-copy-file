def copy_file(command: str):
    command = command.split(" ")
    if len(command) == 3 and command[0] == "cp" and command[1] != command[2]:
        with open(command[1], "r") as source, open(command[2], "w") as target:
            text = source.read()
            target.write(text)
