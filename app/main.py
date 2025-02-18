def copy_file(command: str) -> None:

    str_line = command.split()
    file_read = str_line[1]
    file_write = str_line[2]
    if file_read != file_write:
        with (open(file_read, "r") as file_in,
                open(file_write, "w") as file_out):
            txt = file_in.read()
            file_out.write(txt)
