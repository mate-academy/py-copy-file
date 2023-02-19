def copy_file(command: str) -> None:
    try:
        cp, original_file, file_copy = command.split()
        if original_file != file_copy and cp == "cp":
            with open(original_file) as file1:
                file1 = file1.read()
                if len(file1) != 0:
                    with open(file_copy, "w") as file_copy:
                        file_copy.write(file1)
    except ValueError:
        print("The string must have: command 'cp', file name to copy and new file name")
