def copy_file(str_files: str) -> None:

    first_file = str_files.split(" ")[1]
    another_file = str_files.split(" ")[-1]
    if first_file == another_file:
        return None

    with open(first_file, "r") as file_in, open(another_file, "w") as file_out:
        file_out.write(file_in.read())
