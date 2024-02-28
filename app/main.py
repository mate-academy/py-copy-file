def copy_file(command: str) -> None:
    c_arr = command.rsplit()
    if c_arr[0] == "cp" and (c_arr[1] != c_arr[2]):
        with open(c_arr[1], "r") as file_in, open(c_arr[2], "w") as file_out:
            file_out.write(file_in.read())
