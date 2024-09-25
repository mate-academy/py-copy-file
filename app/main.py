def copy_file(cp: str) -> None:
    file_names = cp.split()
    if file_names[1] != file_names[2] and file_names[0] == "cp":
        try:
            with (
                open(file_names[1]) as file_in,
                open(file_names[2], "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {file_names[1]} does not exist")
