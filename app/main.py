def copy_file(command: str) -> None:
    files = tuple(command.split()[1:])

    if files[0] != files[1]:
        with open(files[0], "r") as file_in, open(files[1], "w") as file_out:
            file_out.write(file_in.read())
