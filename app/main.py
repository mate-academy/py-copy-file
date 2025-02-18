def copy_file(files: str) -> None:
    command, file_1, file_2 = files.split()
    if file_1 != file_2 and command == "cp":
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
