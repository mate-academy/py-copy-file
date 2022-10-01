def copy_file(line: str) -> str:
    command, old_file, new_file = line.split(" ")

    if command != "cp" or old_file == new_file:
        return "Incorrect command or your file names are the same!"

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
