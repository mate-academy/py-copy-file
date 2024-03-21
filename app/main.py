def copy_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "cp":
        return

    input_file, output_file = command.split()[1:]
    if input_file != output_file:
        with (
            open(input_file, "r") as to_copy,
            open(output_file, "w") as copied
        ):
            copied.write(to_copy.read())


copy_file("cp file.txt file.txt")
copy_file("cp file.txt file1.txt file2.txt")
copy_file("file.txt file.txt")
copy_file("cp file.txt new_file.txt")
