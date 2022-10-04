def copy_file(command: str) -> None:
    copy_command, file1, file2 = command.split()

    if copy_command == "cp":
        if file1 != file2:
            with (open(file1, "r") as input_file,
                  open(file2, "w") as output_file):
                output_file.write(input_file.read())
