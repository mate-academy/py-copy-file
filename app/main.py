def copy_file(command: str) -> None:
    file_in = command.split(" ")[1]
    file_out = command.split(" ")[2]
    if file_in != file_out:
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.write(file_in.read())
