def copy_file(command: str) -> None:
    cp, filename, copy_filename = command.split()
    if cp != "cp" and filename != copy_filename:
        with open(filename, "r") as file_in, open(
                copy_filename, "w") as file_out:
            temp = file_in.read()
            file_out.write(temp)
