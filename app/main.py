def copy_file(files: str) -> str:
    command = files.split()[0]
    if command != "cp":
        return "Incorrect command!"
    file_1 = files.split()[1]
    file_2 = files.split()[2]
    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        file_out.write(file_in.read())
    return "Complete"
