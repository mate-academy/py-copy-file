def copy_file(command: str) -> None:
    cp, original_f, copy_f = command.split()
    if cp == "cp" and original_f != copy_f:
        with open(original_f, "r") as file_in, open(copy_f, "w") as file_out:
            file_out.write(file_in.read())
