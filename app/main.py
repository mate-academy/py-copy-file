def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cp, source, target = parts

    if source == target:
        return

    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
