def copy_file(command: str) -> None:
    arguments = command.split()
    if (command.startswith("cp ")
            and len(arguments) == 3
            and arguments[1] != arguments[2]):
        file1 = open(arguments[1], "r")
        file2 = open(arguments[2], "w")
        file2.write(file1.read())
        file1.close()
        file2.close()
