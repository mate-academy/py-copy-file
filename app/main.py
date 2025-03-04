import os


def copy_file(command: str) -> None:
    command_words = command.split()

    if len(command_words) != 3:
        return None

    cp_check = command_words[0]
    first_file = command_words[1]
    second_file = command_words[2]

    if (cp_check == "cp"
            and os.path.exists(first_file)
            and first_file != second_file):

        with open(first_file, "r") as first, open(second_file, "w") as second:
            for line in first:
                second.write(line)

    return None
