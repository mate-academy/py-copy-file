def copy_file(command: str) -> None:
    if not command.strip():
        return
    user_input = command.split()
    prefix = user_input[0]
    if prefix == "cp" and len(user_input) == 3:
        file_in = user_input[1]
        file_out = user_input[2]
        if file_in == file_out:
            return
        else:
            try:
                with (open(file_in, "r") as filin,
                      open(file_out, "w") as filout):
                    filout.write(filin.read())
            except FileNotFoundError:
                return
            except IOError:
                return
    else:
        pass
