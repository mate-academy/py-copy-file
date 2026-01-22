def copy_file(command: str) -> None:
    words = command.split()
    if len(words) == 3 and words[0] == "cp":
        if words[1] != words[2]:
            try:
                with open(words[1], "r") as file:
                    content = file.read()
                with open(words[2], "w") as file:
                    file.write(content)
            except FileNotFoundError:
                pass
