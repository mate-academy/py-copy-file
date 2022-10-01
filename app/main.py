def copy_file(line: str):
    command, old_file, new_file = line.split(" ")

    if old_file == new_file:
        return "Your file names are the same!"
    if command != "cp":
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
