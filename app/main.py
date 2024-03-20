def copy_file(command: str) -> None:
    input_file, output_file = command.split()[1], command.split()[2]
    if input_file != output_file:
        with (
            open(input_file, "r") as to_copy,
            open(output_file, "w") as copied
        ):
            copied.write(to_copy.read())
    return


copy_file("cp file.txt file.txt")
copy_file("cp file.txt new_file.txt")
