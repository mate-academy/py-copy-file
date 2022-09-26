def copyfile_example(command: str) -> None:
    command_name, file_in, file_out = command.split()

    if file_in == file_out:
        return

    with open(file_in, 'r') as source, open(file_out, 'w') as destination:
        destination.write(source.read())
