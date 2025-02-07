def copy_file(command: str) -> None:
    command = command.split(" ")
    file_in = command[1]
    file_out = command[2]
    if file_in != file_out:
        content = None
        with open(file_in, "r") as f:
            content = f.read()

        with open(file_out, "w") as f:
            f.write(content)
