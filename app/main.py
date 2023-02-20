def copy_file(commands: str) -> None:
    command, origin_file, copy_file = commands.split()
    if command == "cp" and origin_file != copy_file:
        with open(origin_file, "r") as content, open(
                copy_file, "w"
        ) as file_in:
            file_in.write(content.read())
