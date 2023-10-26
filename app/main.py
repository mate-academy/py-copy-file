class Error(Exception):
    pass


class FileNameError(Error):
    pass


class CommandError(Error):
    pass


def copy_file(command: str, statring_file_name: str, final_file_name: str) -> None:
    if command != "cp":
        raise CommandError("You privided the wrong command")
    if statring_file_name == final_file_name:
        raise FileNameError("File names can not be equal")
    content_to_copy = " "
    with open(statring_file_name, "r") as file:
        content_to_copy = file.read()
    with open(final_file_name, "w") as file:
        file.write(content_to_copy)
