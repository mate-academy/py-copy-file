def copy_file(command: str) -> None:
    cd, source_name, copy_name = command.split()
    if source_name == copy_name:
        return
    with (open(source_name, "r") as source,
          open(copy_name, "w") as result):
        result.write(source.read())
