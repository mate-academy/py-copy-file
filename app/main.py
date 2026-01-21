def copy_file(command: str) -> None:
    try:
        arguments = command.split(" ")
        if len(arguments) != 3:
            return None

        cmd = arguments[0]
        old_file = arguments[1]
        new_file = arguments[2]
        if cmd != "cp" or old_file == new_file:
            return None

        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            old_file_text = file_in.read()
            file_out.write(old_file_text)
    except FileNotFoundError:
        return None
