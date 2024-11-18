
def copy_file(command: str) -> None:
    parts = command.split()
    filename_in = parts[1]
    filename_out = parts[2]

    if filename_in == filename_out:
        return

    with (open(filename_in, "r") as file_in,
          open(filename_out, "w") as file_out):
        file_out.write(file_in.read())
