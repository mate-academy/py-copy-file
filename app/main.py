def copy_file(line: str) -> None:
    command, old_file, new_file = line.split()
    if (command == "cp") and (old_file != new_file):
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
