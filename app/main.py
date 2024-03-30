def copy_file(command: str) -> None:
    files = command.split(" ")
    if files[1] != files[2]:
        with open(files[1], "r") as file_in, open(files[2], "w") as file_out:
            for_copy = file_in.read()
            file_out.write(for_copy)
