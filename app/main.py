def copy_file(command: str) -> None:
    text_slice = command.split()
    if len(text_slice) != 3 or "cp" != text_slice[0]:
        return
    source = text_slice[1]
    destination = text_slice[2]
    if source == destination:
        return
    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
