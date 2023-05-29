def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "cp":
        _, source_file, file_to_write = command_parts
        if source_file == file_to_write:
            return

        with open(source_file, "r") as source, \
                open(file_to_write, "w") as write_file:
            write_file.write(source.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
