def copy_file(command: str) -> bool:
    command_split = command.split()
    if command_split[0] == "cp":
        if command_split[1] == "file.txt":
            with open("file.txt", "r") as file:
                content = file.read()

            if command_split[2] == "new_file.txt":
                with open("new_file.txt", "w") as file:
                    file.write(content)

    return open("file.txt").read() == open("new_file.txt").read()
