def copy_file(command: str) -> None:
    cp, file_1, file_2 = command.split()
    if file_1 != file_2 and cp == "cp":
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
