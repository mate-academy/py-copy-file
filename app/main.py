def copy_file(command: str) -> None:
    files = command.split(" ")

    if "cp" not in files and files.index("cp") != 0:
        print("Incorrect command to copy file")
        return

    if files[1] == files[2]:
        return None

    with open(files[1], "r") as file, open(files[2], "w") as copying_file:
        copying_file.write(file.read())
