def copy_file(command: str) -> None:
    res = command.split()
    if res[1] != res[2]:
        with open(res[1], "r") as file_in, open(res[2], "w") as file_out:
            file_out.write(file_in.read())
