def copy_file(line: str):
    command, old_file, new_file = line.split(" ")

    if command != "cp":
        return "Wrong command"
    if old_file == new_file:
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
