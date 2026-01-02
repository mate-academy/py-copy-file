def copy_file(command: str) -> None:
    command_list = command.split()
    cp = command_list[0]
    source_name = command_list[1]
    copy_name = command_list[2]

    if (
            len(command_list) != 3
            or cp != "cp"
            or source_name[-3:] != "txt"
            or copy_name[-3:] != "txt"
    ):
        print("The command must be in the following format:")
        print("cp file.txt file-copy.txt")
        return

    if source_name == copy_name:
        print("Name of original file and it's copy must be different")
        return

    with (open(source_name, "r") as source,
            open(copy_name, "w") as copy):
        copy.write(source.read())
