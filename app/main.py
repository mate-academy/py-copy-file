def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, from_file_name, to_file_name = command.split()
        if command == "cp" and from_file_name != to_file_name:
            with open(from_file_name, "r") as from_file, open(to_file_name,
                                                              "w") as to_file:
                source_content = from_file.read()
                to_file.write(source_content)


copy_file("cp test.txt copy.txt")
