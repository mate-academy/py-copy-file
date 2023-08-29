def copy_file(command: str) -> None:
    _, file, new_file = command.split()

    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
