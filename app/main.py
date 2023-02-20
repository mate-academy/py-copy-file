def copy_file(commands: str) -> None:
    command, original_file, copy_file = commands.split()
    if command == "cp" and original_file != copy_file:
        content = open(original_file, "r")
        with open(f"{copy_file}", "w") as source:
            source.write(content.read())
