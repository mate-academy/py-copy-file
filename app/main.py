def copy_file(filename: str) -> None:
    if filename == "":
        return

    file_list = filename.split()
    if len(file_list) != 3 or file_list[0] != "cp":
        return

    source, target = file_list[1], file_list[2]

    try:
        with open(source, "r") as file_in:
            content = file_in.read()
        with open(target, "w") as file_out:
            file_out.write(content)
    except FileNotFoundError:
        print(f"Source file not found: {source}")
        return
