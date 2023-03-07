def copy_file(command: str) -> None:

    str_line = command.split()
    if str_line[1] != str_line[2]:
        with open(str_line[1], "r") as \
                file_in, open(str_line[2], "w") as file_out:
            txt = file_in.read()
            file_out.write(txt)
        file_in.close()
        file_out.close()
