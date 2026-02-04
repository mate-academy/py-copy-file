def copy_file(files: str) -> None:
    _, source, target = files.split()

    if source == target:
        return

    with open(source) as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
