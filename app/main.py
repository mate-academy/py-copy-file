def copy_file(command: str) -> None:
    file_out = command.split(" ")[1]
    file_in = command.split(" ")[2]
    if file_in == file_out:
        pass
    else:
        with open(file_out, "r") as file_out, open(file_in, "w") as file_in:
            file_in.writelines(file_out.readlines())
