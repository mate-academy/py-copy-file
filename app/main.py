def copy_file(command: str) -> None:
    original_file = command.split()[1]
    copy_file = command.split()[2]
    if original_file[0] == "cp" and original_file != copy_file:
        content = open(original_file, "r")
        with open(f"{copy_file}", "w") as source:
            source.write(content.read())
