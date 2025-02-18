def copy_file(command: str) -> None:
    command_words = command.split()

    if not command.startswith("cp") or len(command_words) != 3:
        raise ValueError("Wrong command!")

    if command_words[1] == command_words[2]:
        return

    with (
        open(command_words[1], "r") as file_in,
        open(command_words[2], "w") as file_out
    ):
        file_out.writelines(file_in.readlines())
