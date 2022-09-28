def copyfile_example(command: str) -> None:
    command_name, file_name, file_copy_name = command.split()

    if file_name == file_copy_name:
        return

    with open(file_name, "r") as source, open(file_copy_name, "w") as copy:
        copy.write(source.read())
