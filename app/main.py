def copy_file(command: str) -> None:
    data = command.split()
    if data[1] != data[2] and data[0] == "cp":
        with open(data[1], "r") as file_in, open(data[2], "w") as file_out:
            file_out.write(file_in.read())
