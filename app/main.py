def copy_file(command: str) -> None:
    cp, source, target = command.split()
    if source != target:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())
