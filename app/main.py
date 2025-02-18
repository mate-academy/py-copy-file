

def copy_file(string: str) -> None:
    names = string.split(" ")
    if names[0] == "cp":
        if names[1] != names[2]:
            with open(names[1], "r") as first_file:
                content = first_file.read()
            with open(names[2], "w") as second_file:
                second_file.write(content)
