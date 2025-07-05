def copy_file(command: str) -> None:
    if not command.strip():
        return
    user_input = command.split()
    prefix = user_input[0]
    if prefix == "cp" and len(user_input) == 3:
        file_in = user_input[1]
        file_out = user_input[2]
        if file_in == file_out:
            pass
        else:
            try:
                with (open(file_in, "r") as file_in,
                      open(file_out, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                return
            except IOError:
                return
    else:
        pass
