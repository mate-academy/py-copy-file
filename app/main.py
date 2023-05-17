def copy_file(file_in: str, file_out: str) -> None:
    with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
        file_out.write(file_in.read())
