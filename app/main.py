def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == 'cp':
        first_file = command.split(" ")[1]
        another_file = command.split(" ")[-1]
        if first_file == another_file:
            return None

        with open(first_file, "r") as file_in, open(another_file, "w") as file_out:
            file_out.write(file_in.read())


copy_file("cp text.txt new_text.txt")
