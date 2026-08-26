def copy_file(copy: str) -> None:
    parts = copy.split()
    if len(parts) < 3 or parts[0] != "cp":
        return
    orig_file = parts[1]
    new_file = parts[2]
    if orig_file == new_file:
        return
    try:
        with (open(orig_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
