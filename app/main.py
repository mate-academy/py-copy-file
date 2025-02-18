def copy_file(command: str) -> None:
    cp, filename, copy_name = command.split()
    if cp == "cp" and filename != copy_name:
        with open(filename, "r") as file_in, open(copy_name, "w") as file_out:
            file_out.write(file_in.read())
