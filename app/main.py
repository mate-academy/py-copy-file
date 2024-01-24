def copy_file(command: str) -> None:
    cp, origin_name, copy_name = command.split()
    if cp != "cp" or origin_name == copy_name:
        return
    with open(origin_name, "r") as file_in, open(copy_name, "w") as file_out:
        file_out.write(file_in.read())
