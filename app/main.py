def copy_file(command: str) -> None:
    cmnd, file, file_to_copy = command.split(" ")
    if file != file_to_copy and cmnd == "cp":
        with open(file, "r") as source, open(file_to_copy, "w") as out:
            out.write(source.read())
