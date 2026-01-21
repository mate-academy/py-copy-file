def copy_file(command: str) -> None:
    line = command.split(" ")

    if len(line) != 3 or line[0] != "cp":
        raise ValueError

    file1 = line[1]
    file2 = line[2]

    if file1 == file2:
        print("Source and destination files are the same. No action taken.")
        return
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        for line in file_in:
            file_out.write(line)
