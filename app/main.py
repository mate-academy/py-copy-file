def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cp, file_to_copy, new_file = parts

    if file_to_copy == new_file or cp != "cp":
        return

    with (open(file_to_copy, "r") as file_in,
          open(new_file, "w") as file_out):
        file_out.write(file_in.read())
