class NoCpInCommand(Exception):
    pass


class ArgumentsOutOfRange(Exception):
    pass


def copy_file(command: str) -> None | str:
    sep_file = command.split(" ")
    if len(sep_file) != 3:
        raise ArgumentsOutOfRange
    if sep_file[0] != "cp":
        raise NoCpInCommand
    if sep_file[1] == sep_file[2]:
        return "Does nothing"

    with open(sep_file[1], "r") as file_in, open(sep_file[2], "w") as file_out:
        file_content = file_in.read()
        file_out.write(file_content)
