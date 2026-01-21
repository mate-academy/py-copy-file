def copy_file(command: str) -> None:
    files = command.split()

    if "cp" not in files and files.index("cp") != 0:
        print("Incorrect command to copy file")
        return

    copy_from = files[1]
    copy_to = files[2]

    if copy_from != copy_to:
        with (
            open(copy_from, "r") as copying_file,
            open(copy_to, "w") as copied_file
        ):
            copied_file.write(copying_file.read())
