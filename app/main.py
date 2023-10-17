def copy_file(command: str) -> None:
    splitted = command.split()
    if splitted[0] == "cp" and splitted[1] != splitted[2]:
        file1 = splitted[1]
        file2 = splitted[2]
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
