def copy_file(cp: str) -> None:
    try:
        command, ex_file, new_file = cp.split(" ")
        if ex_file == new_file:
            return None
        if command == "cp":
            with (open(ex_file, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
    except (FileNotFoundError, PermissionError, ValueError):
        return None
