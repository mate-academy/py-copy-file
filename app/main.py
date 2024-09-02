def copy_file(command: str) -> None:
    files = command.strip("cp ").split()
    if files[0] != files[1]:
        with open(files[0], "r") as file_in, open(files[1], "w") as file_out:
            file_out.write(file_in.read())
