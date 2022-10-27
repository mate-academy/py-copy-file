def copy_file(command: str) -> None:
    separate = command.split()
    if separate[1] != separate[2]:
        with open(separate[1], "r") as file_in,\
                open(separate[2], "w") as file_out:
            file_new = file_in.read()
            file_out.write(file_new)
