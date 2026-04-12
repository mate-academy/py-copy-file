def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    file_source = parts[1]
    file_destination = parts[2]
    if file_source == file_destination:
        return
    try:
        with (
            open(file_source, "r") as file_in, open(file_destination, "w")
            as file_out
        ):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
