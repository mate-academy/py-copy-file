def copy_file(command: str) -> None:
    cp, file, new_file = command.split()
    if len(command.split()) == 3 and cp == "cp" and file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
