def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    operation, current_file, new_file = command.split()
    if current_file == new_file:
        return
    else:
        with (
            open(current_file) as input_file,
            open(new_file, "w") as output_file
        ):
            input_file.write(output_file.read())
