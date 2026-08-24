def copy_file(cp: str) -> None:
    cp_file = cp.split()
    if len(cp_file) < 3 or cp_file[0] != "cp":
        return
    orig_file = cp_file[1]
    new_file = cp_file[2]
    if orig_file == new_file:
        return
    try:
        with open(orig_file, "r") as file_in:
            content = file_in.read()
        with open(new_file, "w") as file_out:
            file_out.write(content)
    except FileNotFoundError:
        return
