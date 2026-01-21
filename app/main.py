def copy_file(files: str) -> None:
    ls = files.split()

    if len(ls) != 3 or ls[0] != "cp" or ls[1] == ls[2]:
        return None
    else:
        try:
            with (
                open(ls[1], "r") as file_in,
                open(ls[2], "w") as file_out
            ):
                file_out.write(file_in.read())
                print("File copied successfully")
        except FileNotFoundError:
            return None
