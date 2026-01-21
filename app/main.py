def copy_file(command: str) -> None:
    key_word, source_file, destination_file = command.split()

    if key_word == "cp" or source_file != destination_file:
        with open(source_file, "r") as read_file, \
                open(destination_file, "x") as write_file:
            write_file.writelines(read_file.readlines())
