def copy_file(command: str) -> None:
    files = command.split()
    if open(files[1]) != open(files[2]) and files[0] == "cp":
        with open(files[1], "r") as file_1, open(files[2], "w") as file_2:
            df = file_1.readline()
            for line in df:
                file_2.write(line)
