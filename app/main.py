def copy_file(command: str) -> None:
    cmd, filename, new_filename = command.split()
    if len(command.split()) == 3 or cmd == "cp" or filename != new_filename:
        with open(filename, "r") as file_in, open(new_filename, "w") as file_out:
            file_out.write(file_in.read())
