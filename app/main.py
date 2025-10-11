def copy_file(command: str) -> None:
    copy, paste = command[3:].split(" ")
    if copy != paste:
        with open(paste, "w") as pasted_file:
            with open(copy) as copied_file:
                content = copied_file.read()
            pasted_file.write(content)
