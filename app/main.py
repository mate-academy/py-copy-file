def copy_file(command: str) -> None:
    cp, source, new = command.split(" ")
    if cp != "cp" or source == new:
        return None
    with (
        open(new, "w") as new_file ,
        open(source, "r") as old_file
    ):
        new_file.write(old_file.read())
