def copy_file(command: str) -> None:
    files = command.split(" ")
    if len(files) != 3 or files[0] != "cp":
        return
    file1 = files[1]
    file2 = files[2]
    if file1 != file2:
        try:
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                content = file_in.read()
                file_out.write(content)
        except FileNotFoundError:
            pass
