def copy_file(command: str) -> None:
    split_data = command.split()
    file_in = split_data[1]
    file_out = split_data[2]
    if file_in == file_out:
        pass
    else:
        with (open(file_in, "r", encoding="utf-8") as file_in,
              open(file_out, "w", encoding="utf-8") as file_out):
            file_out.write(file_in.read())
