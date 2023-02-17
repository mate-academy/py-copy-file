def copy_file(command: str) -> None:
    cp, first, second = command.split(" ")
    if first != second and cp == "cp":
        with open(first, "r") as file_in, open(second, "w") as file_out:
            file_out.write(file_in.read())
