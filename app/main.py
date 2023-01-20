def copy_file(command: str) -> None:
    cp, original, copy = command.split()
    if cp == "cp" and original != copy:
        with open(original, "r") as file_in, open(copy, "w") as file_out:
            file_out.write(file_in.read())
