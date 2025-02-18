class CommandError(Exception):
    ...


def copy_file(command: str) -> None:
    content = command.split(" ")
    if content[0] != "cp" or len(content) != 3:
        raise CommandError("Command line error")
    if content[1] != content[2]:
        source_file = content[1]
        destination_file = content[2]
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
