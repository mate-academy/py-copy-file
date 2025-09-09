def copy_file(command: str):
    separar = command.split()
    ind = len(separar)
    if ind == 3 and separar[0] == "cp":
        src = separar[1]
        dst = separar[2]
        try:
            with open(src, "r") as file_in, open(dst, "w") as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError:
            pass
