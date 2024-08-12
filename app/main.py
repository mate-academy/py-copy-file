def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command!")
        return

    if parts[1] == parts[2]:
        return

    with open(parts[1], "r") as f, open(parts[2], "w") as f_copy:
        f_copy.write(f.read())


copy_file("cp file.txt file_copy.txt")
