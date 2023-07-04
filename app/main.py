def copy_file(command: str) -> None:
    parts = command.split()

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    with open(source_file, "r") as file_in:
        content = file_in.read()

    with open(destination_file, "w") as file_out:
        file_out.write(content)


copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())
