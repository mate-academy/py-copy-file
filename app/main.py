def copy_file(command: str) -> None:
    keyword, source_file, target_file = command.split()
    if keyword != "cp" or source_file == target_file:
        return
    with open(source_file, "r") as source_fobj, open(
        target_file, "w"
    ) as target_fobj:
        target_fobj.write(source_fobj.read())
