def copy_file(command: str) -> None:
    command_words = command.split()
    if len(command_words) < 3:
        return
    if command_words[0] != "cp":
        return
    if command_words[1] == command_words[2]:
        return
    source = command_words[1]
    if source is None:
        return
    target = command_words[2]
    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            for line in file_in:
                file_out.write(line)
            file_out.close()
            file_in.close()
    except FileNotFoundError:
        return
