def copy_file(command: str) -> None:
    cp, file, file_copy = command.split(" ")
    if file != file_copy and cp == "cp":
        with open(file, "r") as file_in, open(file_copy, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
