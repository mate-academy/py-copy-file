def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, first_file, second_file = command.split()
        if command and first_file and second_file:
            if command == "cp" and first_file != second_file:
                with (open(first_file, "r") as file,
                      open(second_file, "w") as file_copy):
                    content = file.read()
                    file_copy.write(content)
