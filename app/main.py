def copy_file(command: str) -> None:
    if not command.strip():
        return None
    parts = (command.strip()).split()
    if len(parts) != 3:
        return None
    if parts[0] != "cp":
        return None
    file_in_name = parts[1]
    file_out_name = parts[2]
    if file_in_name != file_out_name:
        try:
            with (
                open(file_in_name, "r") as file_in,
                open(file_out_name, "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return None
