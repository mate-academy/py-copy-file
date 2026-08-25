def copy_file(command: str) -> None:
    command_text = command.split(" ")
    if command_text[0] == "cp":
        if len(command_text) != 3 or command_text[1] == command_text[2]:
            return
        else:
            try:
                with (open(command_text[1], "r") as file1,
                      open(command_text[2], "w") as file2):
                    file2.write(file1.read())
            except FileNotFoundError:
                return
