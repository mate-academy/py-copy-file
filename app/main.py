def copy_file(command: str) -> None:
    cp, file_to_copy, new_file = command.split(" ")
    if cp != "cp" or file_to_copy == new_file:
        print("Not cp command")
        return

    with open(file_to_copy, "r") as f_from, open(new_file, "w") as f_to:
        content = f_from.read()
        f_to.write(content)
