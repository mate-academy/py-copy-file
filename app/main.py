def copy_file(command: str) -> None:
    command_ls = command.split()
    if command_ls[1] == command_ls[2]:
        return
    with open(command_ls[1], "r") as source,\
         open(command_ls[2], "a") as receiver:
        source_contents = source.read()
        receiver.write(source_contents)
