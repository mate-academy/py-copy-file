def copy_file(command: str) -> None:
    check = command.split(" ")
    if len(check) == 3:
        if check[0] != "cp" or check[1] == check[2]:
            return None
        with open(check[1], "r") as file_in, open(check[2], "w") as file_out:
            file_out.write(file_in.read())
