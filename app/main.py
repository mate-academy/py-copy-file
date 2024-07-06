def copy_file(command: str) -> str:
    command = command.split()
    if len(command) != 3:
        return (
            "Please enter a command in "
            "format: 'cp filename.txt new_filename.txt'"
        )
    operation, current_file, new_file = command
    if current_file == new_file:
        return "The name of copy should differ"
    else:
        with (
            open(current_file) as input_file,
            open(new_file, "w") as output_file
        ):
            output_file.write(input_file.read())
