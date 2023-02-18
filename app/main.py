def copy_file(command: str) -> None:
    command_words = command.split()
    if (
            len(command_words) == 3
            and command_words[0] == "cp"
            and command_words[1] != command_words[2]
    ):
        with (
            open(command_words[1], "r") as file_in,
            open(command_words[2], "w") as file_out
        ):
            file_out.write(file_in.read())
