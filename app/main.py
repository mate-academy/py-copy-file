def copy_file(command: str) -> None:
    parts = command.split()
    if (parts[0] != "cp"
            or parts[1] == parts[2]
            or len(parts) != 3):
        return
    with (open(parts[1], "r") as file_in,
          open(parts[2], "w") as file_out):
        file_in_read = "".join(file_in.read())
        file_out.write(str(file_in_read))
