def copy_file(command: str) -> None:
    cp, name, new_name = command.split()
    if cp != "cp":
        return
    if name == new_name:
        return
    with (
        open(name, "r") as source_file,
        open(new_name, "w") as new_file
    ):
        new_file.write(source_file.read())
