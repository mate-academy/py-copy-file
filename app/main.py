def copy_file(cp: str) -> None:
    parts = cp.split(" ")
    old = parts[1]
    new = parts[2]
    if old == new:
        return
    else:
        with open(old, "r") as file_in:
            with open(new, "w") as file_out:
                file_out.write(file_in.read())
