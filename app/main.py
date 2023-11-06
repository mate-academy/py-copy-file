def copy_file(string: str) -> None:
    names = string.split()

    if len(names) == 3 and names[0] == "cp":
        command, source_file, dest_file = names
        if source_file != dest_file:
            with open(source_file, "r") as source_file:
                content = source_file.read()
                with open(dest_file, "w") as destination_file:
                    destination_file.write(content)
