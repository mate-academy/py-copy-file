def copy_file(line: str) -> None:
    com, file1, file2 = line.split()
    if (com == "cp") and (file1 != file2):
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
