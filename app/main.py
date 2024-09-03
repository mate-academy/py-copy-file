def copy_file(command: str) -> None:
    file, file_copy = command.split(" ")[1:3]

    if file == file_copy:
        return

    with open(file, "r") as f, open(file_copy, "w") as fc:
        content = f.read()
        fc.write(content)


command = "cd andrii Suprun.txt"

copy_file(command)
