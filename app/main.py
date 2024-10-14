def copy_file(command: str = "cp") -> None:
    with open(f"{command} file.txt", "r") as r_file:
        with open("new_file.txt", "w") as w_file:
            for line in r_file:
                w_file.write(line)
    r_file.close()
    w_file.close()
