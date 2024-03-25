

def copy_file(file_name: str, new_file: str) -> None:
    if file_name == new_file:
        return
    with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
