def copy_file(cp: str) -> None:
    cp, source_file, new_file = cp.split()
    if source_file == new_file or cp != "cp":
        return
    with open(source_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
