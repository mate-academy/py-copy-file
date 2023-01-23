def copy_file(command: str) -> None:
    splitter = command.split(" ")
    if splitter[0] == "cp" and 3 != len(splitter) \
            and splitter[1] != splitter[2]:
        with open(splitter[1], "r") as file1,\
                open(splitter[2], "w") as file2:
            file2.write(file1.read())
