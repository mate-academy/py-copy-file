def copy_file(command: str) -> None:
    cp, src, dst = command.split()
    if src != dst and cp == "cp":
        with open(src, "r") as file_in, \
                open(dst, "w") as file_out:
            file_out.write(file_in.read())
