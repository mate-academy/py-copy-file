def copy_file(command: str) -> None:
    command = command.split(" ")
    if command[1] == command[2]:
        return
    with open(command[1], "r") as file_def, open(command[2], "w") as file_def2:
        text_file = file_def.read()
        file_def2.write(text_file)
