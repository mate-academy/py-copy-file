def copy_file(command: str) -> None:
    cp, file_to_copy, new_file = command.split(" ")
    if cp != "cp":
        print("Not cp command")
        return
    if file_to_copy == new_file:
        return
    with open(file_to_copy, "r") as f_from, open(new_file, "w") as f_to:
        content = f_from.read()
        f_to.write(content)


copy_file("cp main.py main.bak")
