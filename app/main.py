def copy_file(cp: str) -> None:
    tokens = cp.split()
    if len(tokens) != 3:
        raise ValueError("Invalid command")
    source_file, dest_file = tokens[1], tokens[2]
    if source_file == dest_file:
        return
    with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())
