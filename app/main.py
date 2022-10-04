def copy_file(command: str) -> None:
    existing_file = command.split(" ")[1]
    new_file = command.split(" ")[2]

    if existing_file == new_file:
        return

    with (open(existing_file, "r") as f_read,
          open(new_file, "w") as f_write):
        content = f_read.read()
        f_write.write(content)


copy_file("cp test.txt new_file.txt")
