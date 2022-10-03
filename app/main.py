def copy_file(command: str):
    if command.split()[0] != "cp":
        return f"unknown command: {command.split()[0]}"

    file1 = command.split()[1]
    file2 = command.split()[2]

    if file1 == file2:
        return f"{file1} already exists"

    with open(file1, "r") as f1, open(file2, "w") as f2:
        if f2 is f1:
            return f"{f1} already exists"

        f2.write(f1.read())


copy_file("cp test_lorem.txt new_lorem.txt")
