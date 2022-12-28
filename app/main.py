def copy_file(command: str) -> None:
    _, src, dst = command.split()
    with open(f"{src}", "r") as file_in, \
            open(f"{dst}", "w") as file_out:
        if src != dst:
            file_out.write(file_in.read())


copy_file("cp file.txt file.txt")
