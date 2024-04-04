def copy_file(command: str) -> None:
    _, orig_file, new_file = command.split()
    if orig_file == new_file:
        raise Exception("Copying file into itself is prohibited")
    with open(orig_file, "r") as source, open(new_file, "w") as source_copy:
        for line in source.readlines():
            source_copy.write(line)
