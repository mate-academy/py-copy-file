def copy_file(src: str) -> None:
    command, file_name_in, file_name_out, *_ = src.split()

    if command == "cp" and file_name_in != file_name_out:
        with (open(file_name_in, "r") as file_in,
              open(file_name_out, "w") as file_out):
            file_out.write(file_in.read())
