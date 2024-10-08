def copy_file(command: str) -> None:
    parts = command.split()
    with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
        if parts[1] != parts[2]:
            file_out.write(file_in.read())
