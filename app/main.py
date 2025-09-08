def copy_file(command: str) -> None:
    split_command = command.split(" ")
    file_name = split_command[1]
    copy_name = split_command[2]

    if file_name == copy_name:
        return
    with open(file_name, "r") as target:
        content = target.read()
        with open(copy_name, "w") as copy_target:
            copy_target.write(content)
