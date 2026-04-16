def copy_file(command: str) -> None:
    command_words = command.split()
    if len(command_words) == 3:
        if command_words[0].lower() == "cp":
            file_source = command_words[1]
            file_dest = command_words[2]
            if file_source != file_dest:
                try:
                    with (
                        open(file_source, "r") as file_source,
                        open(file_dest, "w") as file_dest
                    ):
                        file_dest.write(file_source.read())
                except FileNotFoundError:
                    pass
