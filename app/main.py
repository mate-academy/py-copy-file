def copy_file(command: str) -> None:
    file_r = command.split(" ")[1]
    file_w = command.split(" ")[2]
    if file_r != file_w:
        with open(file_r, "r") as file_in, open(file_w, "w") as file_out:
            file_out.write(file_in.read())
