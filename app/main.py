def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "cp":
        first, second, third = command.split()
        if second != third:
            try:
                with open(second, "r") as first_file, \
                        open(third, "w") as second_file:
                    content = first_file.read()
                    second_file.write(content)
            except FileNotFoundError:
                print("The file does not exist.")
