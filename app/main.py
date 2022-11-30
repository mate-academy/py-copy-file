from os.path import exists


def copy_file(command: str) -> None:
    tokens = command.split(" ")

    if len(tokens) != 3:
        return

    command = tokens[0]
    name_of_original = tokens[1]
    name_of_copied = tokens[2]

    if (
        not exists(name_of_original)
        or command != "cp"
        or name_of_original == name_of_copied
    ):
        return

    with (
        open(name_of_original, "r") as file_in,
        open(name_of_copied, "w") as file_out
    ):
        file_out.write(file_in.read())
