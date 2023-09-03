def copy_file(filename: str) -> None:
    file_for_copy = filename.split(" ")[1]
    new_file = filename.split(" ")[2]
    with open(file_for_copy, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
