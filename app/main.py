def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    src_file = parts[1]
    dest_file = parts[2]
    if src_file == dest_file:
        return
    with (
        open(src_file, mode="r") as file_in,
        open(dest_file, mode="w") as file_out
    ):
        content = file_in.read()
        file_out.write(content)
