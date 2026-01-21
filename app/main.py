def copy_file(command: str) -> None:
    splitted_string = command.split()
    if splitted_string[1] != splitted_string[2]\
            and command.startswith("cp"):
        with open(splitted_string[1], "r") as file_in, \
                open(splitted_string[2], "w") as file_out:
            info = file_in.read()
            file_out.write(info)
