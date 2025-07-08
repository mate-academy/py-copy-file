def copy_file(command: str) -> None:
    try:
        command, src_filename, dst_filename = command.split()
    except ValueError:
        return

    if command != "cp" or src_filename == dst_filename:
        return

    try:
        with (open(src_filename, "r") as src_file,
              open(dst_filename, "w") as dst_file):
            dst_file.write(src_file.read())
    except FileNotFoundError:
        return
