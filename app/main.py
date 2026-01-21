def copy_file(command: str) -> None:
    file_command = command.split()
    if len(file_command) == 3:
        first_file = file_command[1]
        second_file = file_command[2]
        if file_command[0] == "cp" and first_file != second_file:
            with (open(first_file, "r") as file1,
                  open(second_file, "w") as file2):
                file2.write(file1.read())
