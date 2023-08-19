def copy_file(command: str) -> None:
    parts = command.split()
    name1 = parts[1]
    name2 = parts[2]
    if name1 == name2:
        print("Incorrectly")
    else:
        with open(name1, "r") as file_in, open(name2, "w") as file_out:
            file_out.write(file_in.read())
