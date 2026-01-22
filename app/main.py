import os


def copy_file(command: str) -> None:
    command_words = command.split()
    if (len(command_words) == 3
        and command_words[1] != command_words[2]
        and os.path.exists(command_words[1])
        and command_words[0] == "cp"): # noqa: E129 E261
        with (open(command_words[1], "r") as file_read,
              open(command_words[2], "w") as file_write):
            file_write.write(file_read.read())
    pass
