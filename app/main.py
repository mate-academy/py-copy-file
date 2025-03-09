def copy_file(command: str) -> None:
    files_name = command.split()

    if len(files_name) < 3 or files_name[0] != "cp":
        return None

    src_file_name = files_name[1]
    dest_file_name = files_name[2]

    if src_file_name == dest_file_name:
        return None
    try:
        with open(src_file_name, "r") as src, \
                open(dest_file_name, "w") as dest:
            for line in src:
                dest.write(line)
    except FileNotFoundError:
        print(f"No such file or directory: {src_file_name}")
