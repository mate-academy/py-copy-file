def copy_file(command: str) -> None:
    command, file_out, file_in = command.split()
    if file_out != file_in:
        with (open(file_out, "r") as f_in,
              open(file_in, "w") as f_out):
            content = f_in.read()
            f_out.write(content)
