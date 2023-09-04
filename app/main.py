def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source, new_source = parts[1], parts[2]

    if source == new_source:
        return

    with open(source, "r") as file_in, open(new_source, "w") as file_out:
        file_out.write(file_in.read())
