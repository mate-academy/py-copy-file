def copy_file(command: str) -> None:
    command_text = command.split()
    if len(command_text) != 3:
        return
    try:
        source, dest = command_text[1], command_text[2]
        if source == dest:
            return
        if command_text[0] == "cp":
            with open(source, "r") as file_in, open(dest, "w") as file_out:
                for line in file_in:
                    file_out.write(line)
    except FileNotFoundError:
        return