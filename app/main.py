def copy_file(command: str) -> None:
    name_1, name_2 = command.split(" ")[1:]
    if name_1 == name_2:
        return

    with open(name_1, "r") as file_in, open(name_2, "w") as file_out:
        file_out.write(file_in.read())
