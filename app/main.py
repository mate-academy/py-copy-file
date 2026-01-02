def copy_file(command: str) -> None:
    names = command.split(" ")
    file_in = names[1]
    file_out = names[2]
    if file_in == file_out:
        pass
    else:
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.writelines(file_in.readlines())
