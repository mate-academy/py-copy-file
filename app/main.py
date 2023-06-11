from os import path


class CopyCommandSyntaxError(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split()

    if command[0] != "cp":
        raise CopyCommandSyntaxError("Copy command not found")

    if len(command) != 3:
        raise CopyCommandSyntaxError(
            "Invalid copy command syntax.\n"
            "For a successful copy "
            "the command should look like this: "
            "cp file.txt file-copy.txt"
        )

    file_to_copy = command[1]

    if not path.exists(file_to_copy):
        raise FileNotFoundError(f"File {file_to_copy} does not exist")

    new_file = command[-1]

    if file_to_copy != new_file:
        with open(file_to_copy, "r") as source, open(new_file, "w") as copy:
            copy.write(source.read())
