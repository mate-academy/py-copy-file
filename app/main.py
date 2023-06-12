def copy_file(command: str) -> None:
    source, target = command.split()[1:]

    if source != target:
        with open(source, "rb") as file_in, open(target, "wb") as file_out:
            file_out.write(file_in.read())
