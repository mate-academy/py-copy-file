def copy_file(file_names: str) -> None:
    names = file_names.split()
    if names[0] != "cp" or names[1] == names[2]:
        return None
    with open(names[1], "r") as file_in, open(names[2], "w") as file_out:
        file_out.writelines(file_in.read())
