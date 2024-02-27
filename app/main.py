def copy_file(command: str) -> None:
    split = command.split()
    if split[1] != split[2] and split[0] == "cp" and len(split) == 3:
        with open(split[1], "r") as file_in, open(split[2], "w") as file_out:
            file_out.write(file_in.read())
