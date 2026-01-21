def copy_file(files: str) -> None:
    files_split = files.split()
    if len(files_split) < 3:
        return
    file_obj = files_split[1]
    file_new = files_split[2]
    command = files_split[0]
    if file_obj == file_new:
        return
    try:
        if command == "cp":
            with (open(file_obj, "r") as f,
                  open(file_new, "w") as f_cp):
                for line in f:
                    f_cp.write(line)
    except FileNotFoundError:
        return
    return
