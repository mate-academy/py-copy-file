def copy_file(command: str) -> None:
    args = command.split(" ")
    com = args[0]
    file_copy = args[1]
    new_file = args[2]

    if com == "cp" and file_copy != new_file:
        with open(file_copy, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
