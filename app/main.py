def copy_file(line: str) -> None:
    f_names = line.split(" ")
    print(f_names)
    if (f_names[0] == "cp") and (f_names[1] != f_names[2]):
        with open(f_names[1], "r") as file_in, \
                open(f_names[2], "w") as file_out:
            file_out.write(file_in.read())
