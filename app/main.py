def copy_file(command: str) -> None | str:
    command_name, file_in, file_out = command.split()

    if command_name != "cp" or file_in == file_out:
        print("Does nothing")
        return "Does nothing"

    with open(file_in, "r") as fi, open(file_out, "w") as fo:
        fo.write(fi.read())
