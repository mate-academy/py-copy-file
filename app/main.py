def copy_file(line: str) -> None:
    if line == "":
        return
    else:
        line_list = line.split(" ")
        file1 = line_list[1]
        file2 = line_list[-1]
    try:
        open(file1, "r")
    except FileNotFoundError:
        return
    else:
        if file1 != file2 and line_list[0] == "cp" and len(line_list) == 3:
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                file_out.write(file_in.read())
