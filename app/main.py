def copy_file(command: str) -> None:
    command = command[3:].split(" ")
    f_in = str(command[0])
    f_out = str(command[1])

    with open(f_in, "r") as file_in, open(f_out, "w") as file_out:
        if f_in != f_out:
            tmp = file_in.read()
            file_out.write(tmp)
