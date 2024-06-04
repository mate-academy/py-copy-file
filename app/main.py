def copy_file(command: str) -> None:
    command = command.split(" ")
    copy_file = command[1]
    new_file = command[2]
    if copy_file == new_file:
        new_file = "new_" + command[2]

    content = []
    with open(copy_file) as f:
        lines = f.readlines()

        for line in lines:
            content.append(line)

    with open(new_file, "w") as f:
        f.writelines(content)
