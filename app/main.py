

def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    operation, source_filename, destination_filename = parts

    if operation != "cp" or source_filename == destination_filename:
        return

    try:
        with (open(source_filename, "rb") as file_in,
              open(destination_filename, "wb") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
