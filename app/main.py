def copy_file(string: str) -> None:
    names = string.split(" ")
    if len(names) >= 3 and names[0] == "cp":
        source_file, dest_file = names[1], names[2]

        if source_file != dest_file:
            with open(source_file, "r") as first_file:
                content = first_file.read()
            with open(dest_file, "w") as second_file:
                second_file.write(content)
