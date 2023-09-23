def copy_file(command: str) -> None:
    content = command.split()
    if content[0] == "cp" and content[1] != content[2]:
        with open(content[1], "rb") as src_file, (
                open(content[2], "wb")
        ) as dest_file:
            while True:
                data = src_file.read()
                if not data:
                    break
                dest_file.write(data)
